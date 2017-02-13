import falcon
import json
from pyfirmata import Arduino, util

l_motor_speed = 0
r_motor_speed = 0

l_motor
l_dir1 = 2
l_dir2 = 3

r_motor
r_dir1 = 4
r_dir2 = 5

board

left_dir1_pin
left_dir2_pin
left_pwm

right_dir1_pin
right_dir2_pin
right_pwm

def get_status():
    return 'POST -> Left Motor: ' + str(l_motor_speed) + ', Right Motor: ' + str(r_motor_speed)

def set_l_motor(speed):
    global l_motor_speed
    print 'Setting Left Motor to: ' + str(speed)
    l_motor_speed = speed
    
def set_r_motor(speed):
    global r_motor_speed
    print 'Setting Right Motor to: ' + str(speed)
    r_motor_speed = speed

def setup(device_path):
    global board
    global left_dir1_pin
    global left_dir2_pin
    global left_pwm
    global right_dir1_pin
    global right_dir2_pin
    global right_pwm
    global l_motor
    global l_dir1
    global l_dir2
    global r_motor
    global r_dir1
    global r_dir2

    board = Arduino(device_path)

    left_dir1_pin = board.get_pin('a:' + l_dir1 + ':i')
    left_dir2_pin = board.get_pin('a:' + l_dir2 + ':i')
    left_pwm = board.get_pin('d:' + l_motor + ':p')

    right_dir1_pin = board.get_pin('a:' + r_dir1 + ':i')
    right_dir2_pin = board.get_pin('a:' + r_dir2 + ':i')
    right_pwm = board.get_pin('d:' + r_motor + ':p')

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
