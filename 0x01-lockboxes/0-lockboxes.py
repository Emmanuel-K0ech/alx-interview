#!/usr/bin/python3
"""LockBoxes Puzzle - interview Problem """


def next_opened_box(opened_boxes):
    """Looks for the next opened box"""
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    b_aux = {}
    while True:
        if len(b_aux) == 0:
            b_aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = next_opened_box(b_aux)
        if keys:
            for key in keys:
                try:
                    if b_aux.get(key) and b_aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    b_aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in b_aux.values()]:
            continue
        elif len(b_aux) == len(boxes):
            break
        else:
            return False

    return len(b_aux) == len(boxes)


def main():
    """Point of Entry"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
