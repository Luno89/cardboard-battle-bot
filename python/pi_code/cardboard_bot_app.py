import falcon
import json

l_motor = 0
r_motor = 0

def get_status():
    return 'POST -> Left Motor: ' + str(l_motor) + ', Right Motor: ' + str(r_motor)

def set_l_motor(speed):
    global l_motor
    print 'Setting Left Motor to: ' + str(speed)
    l_motor = speed
    
def set_r_motor(speed):
    global r_motor
    print 'Setting Right Motor to: ' + str(speed)
    r_motor = speed

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
        set_l_motor(int(result_json['l_motor']))
        set_r_motor(int(result_json['r_motor']))
        resp.body = json.dumps(get_status(), encoding='utf-8')
    
api = falcon.API()

bot_resource = CardBoardBotResource()

api.add_route('/bot', bot_resource)
