# -*- coding: utf8 -*-

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

ImageId = ""
InstanceId = ""
secretId = ""
secretKey = ""


def main_handler(event, context):
    try:
        cred = credential.Credential(secretId, secretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cvm_client.CvmClient(cred, "ap-shanghai", clientProfile)

        req = models.ResetInstanceRequest()
        params = '{"InstanceId":"%s","ImageId":"%s","LoginSettings":{"KeepImageLogin":"TRUE"}}' % (InstanceId, ImageId)
        req.from_json_string(params)

        resp = client.ResetInstance(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)
