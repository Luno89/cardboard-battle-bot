import falcon
import json

l_motor = 0
r_motor = 0

class CardBoardBotResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Left Motor: %s, Right Motor: %s' % (l_motor,r_motor)
                     
    
    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Error',
                                   ex.message)
        
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode. JSON was incorrect')
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(result_json['username'], encoding='utf-8')
        
api = falcon.API()

bot_resource = CardBoardBotResource()

api.add_route('/bot', bot_resource)
