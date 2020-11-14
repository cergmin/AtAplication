from PyQt5 import QtCore, QtWidgets


class QClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()
 
    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


get_verdict_info = {
    # short_name: [full_name, color]
    'OK': ['Тест пройден', 'hsl(115, 92%, 23%)'],
    'WA': ['Wrong answer', 'hsl(0, 92%, 25%)'],
    'PE': ['Presentation error', 'hsl(70, 100%, 23%)'],
    'TL': ['Time limit', 'hsl(70, 100%, 23%)'],
    'ML': ['Memory limit', 'hsl(70, 100%, 23%)'],
    'RE': ['Runtime error', 'hsl(300, 92%, 25%)'],
    'CE': ['Compilation error', 'hsl(190, 92%, 25%)'],
    'FL': ['Fall', 'hsl(0, 92%, 25%)'],
    'NP': ['Не проверено', 'hsl(0, 0%, 20%)']
}


def cut(s, max_len, ending='...'):
    s = str(s)
    ending = str(ending)

    if len(s) <= max_len:
        return s
    return s[:max_len - len(ending)] + ending


def cut_path(path, max_len, sep='/'):
    path = str(path)
    sep = str(sep)

    if len(path) <= max_len:
        return path

    path = path.split(sep)
    start = path[0]
    end = path[-1]
    path_out = []
    
    if len(end) >= max_len or \
       (len(start) + len(end) + (5 if len(path) > 2 else 1)) > max_len:
        return end
    
    if (len(start) + len(end) + (5 if len(path) > 2 else 1)) > max_len:
        return start + (sep + '...' + sep if len(path) > 2 else sep) + end
    
    for i in path[-2:1:-1]:
        path_out += [i]
        if len(sep.join(path_out)) > max_len - len(path[0]) - 1:
            path_out = path_out[:-1]
            break
    
    path_out.reverse()
    path_out = [start, '...'] + path_out + [end]
    return sep.join(path_out)