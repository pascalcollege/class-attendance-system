"""
-- Created by: Ashok Kumar Pant
-- Email: asokpant@gmail.com
-- Created on: 11/06/2024
"""

from demoservice.api.settings import ALLOWED_EXTENSIONS
from demoservice.irs.entities import IRRequest, BaseRequest
from fastapi import Request, UploadFile, HTTPException
from treeutil.logging import TreeLogger

logger = TreeLogger(__name__)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def build_response(response):
    from flask import jsonify
    try:
        return jsonify(response.get_dict())
    except TypeError as _:
        return jsonify(response.__dict__)


async def parse_request(request: Request):
    try:
        base_request = BaseRequest()
        form = await request.form()
        files = form.getlist("file")
        if len(files) > 0:
            base_request.files = files
        file_urls = form.getlist("file_url")
        if len(file_urls) > 0:
            base_request.file_urls = file_urls
        done = len(form) > 0
        if not done and request.headers.get("content-type", None) == "application/json":
            body = await request.json()
            if len(body) > 0:
                base_request.jsn = body
        return base_request
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail="Bad request")


async def parse_file_request(file: UploadFile = None, file_url: str = None,
                             input_text: str = None, payload: IRRequest = None):
    try:
        base_request = BaseRequest()
        if file is not None:
            base_request.files = [file]
        if file_url is not None:
            base_request.file_urls = [file_url]
        if input_text is not None:
            base_request.input_text = input_text
        if payload is not None:
            base_request.body = payload
        return base_request
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail="Bad request")
