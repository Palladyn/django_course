from django.http import HttpRequest

def set_useragent_on_req_middleware(get_response):
    # print("init")
    def middlewate(request:HttpRequest):
        # print("def")
        request.user_agent=request.META["HTTP_USER_AGENT"]
        responce=get_response(request)
        # print("end_def")
        return responce
    # print("end")
    return middlewate


class CountRequestsMidlware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.req_count=0
        self.resp_count=0
        self.exept_count=0

    def __call__(self, request:HttpRequest):
        self.req_count=self.req_count+1
        print(f"requests={self.req_count}")
        resp=self.get_response(request)
        self.resp_count=self.resp_count+1
        print(f"respons={self.resp_count}")
        return resp

    def process_exception(self, request:HttpRequest,exception:Exception):
        self.exept_count=self.exept_count+1
        print(f"exepts={self.resp_count}")
