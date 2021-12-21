from pusher import Pusher

pusher_client = Pusher(app_id='1240328', key='5da93eb6edec4c278dc3', secret='f62aa860566bb9e91b44', cluster='eu')

def sendOrder(orderJson):
    print(type(orderJson))
    pusher_client.trigger('mustang-orders', 'mustang-order', orderJson)