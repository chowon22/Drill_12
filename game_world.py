# 객체로 구성된 게임 월드
# world = [] 게임월드에 존재하는 모든 객체를 담는 리스트
#계층적 구조를 갖는 게임 월드
world = [[] , []]

# 게임 월드에 객체를 담는 함수
def add_object(o, depth=0):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise Exception("Object not found")


def update():
    for layer in world:
        for o in layer[:]:  # update 중에 객체가 제거될 수 있으므로 복사본을 순회
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()


