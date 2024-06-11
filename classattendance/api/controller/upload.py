"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 2/6/20
"""
import os
import shutil
from io import BytesIO

import requests
from fastapi import APIRouter
from treeutil import ioutil, strutil
from treeutil.logging import TreeLogger
from treeutil.timer import Timer
from treeutil.util import get_uuid
from werkzeug.utils import secure_filename

from demoservice.api import helper, settings
from demoservice.entities.api import FileUploadBaseRequest, ApiResponse
from demoservice.entities.file_detail import FileDetail

from classattendance.utils.logger import Logger

logger = Logger.get_logger(__name__)
router = APIRouter()


def download_single_file(file_url, file_name=None):
    if file_name is None:
        try:
            filename = file_url.split("?")[0].split("/")[-1]
        except Exception as e:
            filename = get_uuid() + ".pdf"
    else:
        filename = file_name

    if not helper.allowed_file(filename):
        return FileDetail(error=True, msg="Invalid file format. Allowed extensions : " + str(
            settings.ALLOWED_EXTENSIONS))

    response = requests.get(file_url)
    file_content = BytesIO(response.content)

    filepath = os.path.join(settings.UPLOAD_DIRECTORY, filename)
    success = ioutil.save_bytesio_to_file(file_content, filepath)
    if not success:
        file_detail = FileDetail(error=True, msg="Unable to load file from url: {}".format(file_url))
    else:
        file_detail = FileDetail(error=False, file_url=file_url, file_path=filepath, file_name=filename)
    return file_detail


def upload(request: FileUploadBaseRequest):
    timer = Timer()
    timer.tic()
    try:
        logger.debug("Upload Request:{}".format(request))
        if request.files is not None:
            results = []
            for file in request.files:
                if strutil.is_empty(file.filename):
                    return ApiResponse(error=True, msg="File not selected")
                elif helper.allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    uploaded_filename = os.path.join(settings.UPLOAD_DIRECTORY, filename)
                    with open(uploaded_filename, 'wb+') as fp:
                        shutil.copyfileobj(file.file, fp)
                    result = FileDetail(error=False, file_path=uploaded_filename)
                else:
                    result = FileDetail(error=True, msg="Invalid file format. Allowed extensions : " + str(
                        settings.ALLOWED_EXTENSIONS))
                results.append(result)
            return ApiResponse(error=False, result=results)
        elif request.file_urls is not None:
            results = []
            for file_url in request.file_urls:
                response = requests.get(file_url)
                pdf_file = BytesIO(response.content)
                try:
                    filename = file_url.split("?")[0].split("/")[-1]
                except Exception as e:
                    filename = get_uuid() + ".pdf"
                filename = os.path.join(settings.UPLOAD_DIRECTORY, filename)
                success = ioutil.save_bytesio_to_file(pdf_file, filename)
                if not success:
                    return ApiResponse(error=True, msg="Unable to load file from url: {}".format(file_url))
                if helper.allowed_file(filename):
                    result = FileDetail(file_path=filename, file_url=file_url)
                    results.append(result)
                else:
                    result = FileDetail(error=True, msg="Invalid file format. Allowed extensions : " + str(
                        settings.ALLOWED_EXTENSIONS))
                    results.append(result)
            return ApiResponse(error=False, result=results)
        elif request.file_path is not None:
            return ApiResponse(error=False, result=[FileDetail(file_path=request.file_path)])
        elif request.jsn is not None:
            files = request.jsn.get('files', {})
            results = []
            for file in files:
                file_detail = FileDetail.parse_obj(file)
                result = download_single_file(file_detail.file_url)
                results.append(result)
            return ApiResponse(error=False, result=results)
        elif request.body is not None:
            results = [download_single_file(request.body.file.file_url, file_name=request.body.file.file_name)]
            return ApiResponse(error=False, result=results)
        else:
            return ApiResponse(error=True, msg="Invalid input.")
    except Exception as e:
        logger.exception("Error while uploading the file. {}".format(e))
    logger.debug("Upload time: {} sec.".format(timer.toc(average=False)))
    return ApiResponse(error="true", msg="Error while uploading the file")
