from mitmproxy import http
import json
class Unban:
    def __init__(self):
        self.bannedplugin_keyword='bannedplugin'
        self.chetplugin_keyword='cheatplugin'
        self.asset_meta_keyword='Asset/Meta'
    def response(self,flow:http.HTTPFlow):
        #detect hash checking
        if self.asset_meta_keyword in flow.request.pretty_url:
            res=json.loads(flow.response.text)
            assets=res['Assets']
            for asset in assets:
                if 'bannedplugin.json' in asset['FileName']:
                    print('filename found,modifying')
                    asset['Hash']='8ffc185ec1cae72bf30b6490d489a520d5bdbfc1'.upper()
                elif 'cheatplugin.json' in asset['FileName']:
                    print('filename found,modifying')
                    asset['Hash']='d416be7ffea7451d10ff744e621db7345ceec16d'.upper()
                continue
            flow.response.set_text(json.dumps(res))
            print (flow.response.text)
        #detect banlist checking
        if self.bannedplugin_keyword in flow.request.pretty_url:
            print('keyword : bannedplugin detected')
            print (flow.request.pretty_url)
            print ('injacking....')
            flow.response.set_text(json.dumps([{"Name": "asdfw","AssemblyVersion": "1.0"}]))
            print (flow.response.text)
        #detect cheatlist checking
        if self.chetplugin_keyword in flow.request.pretty_url:
            print('keyword : bannedplugin detected')
            print (flow.request.pretty_url)
            print ('injacking....')
            flow.response.set_text(json.dumps([{"Name": "53F809A7DAC","AssemblyVersion": "0.0.0.0"}]))
            print (flow.response.text)
        
                
                
