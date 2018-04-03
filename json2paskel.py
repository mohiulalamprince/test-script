import json
from collections import namedtuple

file_pointer = open("new-json-file.json", "r")
#file_pointer = open("json-file.json", "r")
#file_pointer = open("dial.json", "r")
#file_pointer = open("getKey.json", "r")

json_object = json.load(file_pointer, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

pascal = ""

def depth2tab(depth):
    tabs = ""
    for d in range(depth):
        tabs += "\t"
    return tabs

def is_play(children):
    try:
        if children.name == 'play':
            return True
        else:
            return False
    except:
        return False

def is_record(children):
    try:
        if children.name == 'record':
            return True
        else:
            return False
    except:
        return False

def is_menu(children):
    try:
        if children.name == 'menu':
            return True
        else:
            return False
    except:
        return False

def is_getKey(children):
    try:
        if children.name == 'getKey':
            return True
        else:
            return False
    except:
        return False

def is_dial(children):
    try:
        if children.name == 'dial':
            return True
        else:
            return False
    except:
        return False

def is_hangup(children):
    try:
        if children.name == 'hangup':
            return True
        else:
            return False
    except:
        return False

def is_case(children):
    try:
        if children.name == 'case':
            return True
        else:
            return False
    except:
        return False

def is_let(children):
    try:
        if children.name == 'let':
            return True
        else:
            return False
    except:
        return False

def is_testIF(children):
    try:
        if children.name == 'test':
            return True
        else:
            return False
    except:
        return False

def is_week(children):
    try:
        if children.name == 'week':
            return True
        else:
            return False
    except:
        return False

def is_year(children):
    try:
        if children.name == 'year':
            return True
        else:
            return False
    except:
        return False

def is_do(children):
    try:
        if children.name == 'do':
            return True
        else:
            return False
    except:
        return False

def is_return(children):
    try:
        if children.name == 'return':
            return True
        else:
            return False
    except:
        return False

def is_execute(children):
    try:
        if children.name == 'execute':
            return True
        else:
            return False
    except:
        return False

def is_repeat(children):
    try:
        if children.name == 'repeat':
            return True
        else:
            return False
    except:
        return False

def is_break(children):
    try:
        if children.name == 'break':
            return True
        else:
            return False
    except:
        return False

def is_sequence(children):
    try:
        if children.name == 'sequence':
            return True
        else:
            return False
    except:
        return False

def get_continue_after_hangup(parent):
    continueAfterHangup = ''
    try:
        if parent.data.ontinueAfterHangup:
            continueAfterHangUp = '-cont'
        return continueAfterHangup
    except: return ''

def get_stop_on_dtmf(parent):
    stopOnDtmf = 0
    try:
        if parent.data.stopOnDtmf:
            stopOnDtmf = 1
        return stopOnDtmf
    except: return 0

def get_max_key(parent):
    maxKey = 0
    try:
        if parent.data.axkey:
            maxKey = parent.data.maxkey
        return maxKey
    except: return 0

def get_max_ring_val(parent):
    maxringval = 0
    try:
        if parent.data.maxringval:
            maxringval = parent.data.maxringval
        return maxringval
    except: return 0

def get_dial(parent):
    dial = 0
    try:
        if parent.data.dial:
            dial = parent.data.dial
        return dial
    except: return 0

def get_go_off_hook(parent):
    gooffhook = 0
    try:
        if parent.data.gooffhook:
            dial = parent.data.gooffhook
        return gooffhook
    except: return 0

def get_directory_path(parent):
    directoryPath = ''
    try:
        if parent.data.directoryPath:
            directoryPath = '"' + parent.data.directoryPath + '"'
        return directoryPath
    except: return directoryPath

def get_timeout_duration(parent):
    timeoutDuration = ''
    try:
        if parent.data.timeoutDuration:
            timeoutDuration = '-time ' + parent.data.timeoutDuration
        return timeoutDuration
    except: return ''

def make_play_pascal_code(parent, depth):
    continueAfterHangup = get_continue_after_hangup(parent)
    stopOnDtmf = get_stop_on_dtmf(parent)
    directoryPath = get_directory_path(parent)

    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Play file"\n'
    pascal_code += depth2tab(depth) + 'play "%s" %s -keys %s %s\n' % (parent.data.filename, directoryPath, stopOnDtmf, continueAfterHangup)
    pascal_code += make_pascal(parent.child, depth + 1)
    pascal_code += depth2tab(depth-1) + '}\n'
    
    return pascal_code

def make_getKey_pascal_code(parent, depth):
    maxKey = get_max_key(parent)
    timeoutDuration = get_timeout_duration(parent)
    continueAfterHangup = get_continue_after_hangup(parent)

    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Get Key"\n'
    pascal_code += depth2tab(depth) + 'getKey Key %s %s %s\n' % (maxKey, timeoutDuration, continueAfterHangup)
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_dial_pascal_code(parent, depth):
    dial = get_dial(parent)
    maxringval = get_max_ring_val(parent)
    gooffhook = get_go_off_hook(parent)

    if maxringval > 0:
        maxringval = '-rings %s' % maxringval

    pascal_code = depth2tab(depth-1) + "{\n"
    if gooffhook:
        pascal_code += depth2tab(depth) + 'offhook\n'
    pascal_code += depth2tab(depth) + '!"Dial"\n'
    pascal_code += depth2tab(depth) + 'dial "%s" %s\n' % (dial, maxringval)
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_hangup_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + 'hangup\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_case_pascal_code(parent, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Case"\n'
    
    for index, children in enumerate(parent.children):
        if is_play(children):
            pascal_code += depth2tab(depth) + 'if Key = "%s"' % str(int(index) + 1)
            pascal_code += make_play_pascal_code(children, depth + 1)
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_let_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Let"\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_testIF_pascal_code(parent, depth):
    pascal_code = depth2tab(depth-1) + "{\n"

    pascal_code += depth2tab(depth) + '!"Test"\n'
    for children in parent.items:
        if children.condition == True:
            pascal_code += depth2tab(depth) + 'if 12345\n'
        else:
            pascal_code += depth2tab(depth) + 'else\n'
        pascal_code += make_pascal(children.branch, depth + 1)
    pascal_code += depth2tab(depth) + 'fi\n'
    
    pascal_code += make_pascal(parent.child, depth + 1)
    pascal_code += depth2tab(depth-1) + '}\n'
    
    return pascal_code

def make_week_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Check week"\n'
    pascal_code += depth2tab(depth) + 'checkweek "some calender" nvt_call_client\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_year_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Check week"\n'
    pascal_code += depth2tab(depth) + 'checkschedule nvt_year nvt_year\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_do_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Module call:"\n'
    pascal_code += depth2tab(depth) + 'do "program1"\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_return_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + 'return\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_execute_pascal_code(children, depth):
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Exec"\n'
    pascal_code += depth2tab(depth) + 'run "program 1"\n'
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_repeat_pascal_code(parent, depth):
    pascal_code = depth2tab(depth-1) + "int nvd_brk_1\n"
    pascal_code += depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"WhileEx"\n'
    pascal_code += depth2tab(depth) + 'nvd_brk_1 = 0\n'
    pascal_code += depth2tab(depth) + 'nvd_loop1 = 0\n'

    while_condition = parent.data.whileCondition
    if while_condition != "":    
        pascal_code += depth2tab(depth) + 'while %s and nvd_brk_1 = 0\n' % while_condition
    
    count = parent.data.count
    if count > 0:
        pascal_code += depth2tab(depth) + 'while nvd_loop1 < %s and nvd_brk_1 = 0\n' % count
        pascal_code += depth2tab(depth + 1) + 'nvd_loop1 = nvd_loop1 + 1\n'

    looptype = parent.data.looptype
    if looptype == 'endless':
        pascal_code += depth2tab(depth) + 'while nvd_brk_1 = 0\n'

    for children in parent.items:
        pascal_code += make_pascal(children, depth + 2) 
    
    pascal_code += make_pascal(parent.child, depth + 1)
    pascal_code += depth2tab(depth) + 'wend\n'
    pascal_code += depth2tab(depth-1) + '}\n'
    
    return pascal_code

def make_break_pascal_code(children, depth):
    pascal_code += depth2tab(depth) + 'nvd_loop2 = 1\n'

    return pascal_code

def make_sequence_pascal_code(parent, depth):
    pascal_code += depth2tab(depth-1) + '{\n'

    for children in parent.children:
        pascal_code += make_pascal(children, depth + 1) 
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_record_pascal_code(parent, depth):
    continueAfterHangup = get_continue_after_hangup(parent)
    stopOnDtmf = get_stop_on_dtmf(parent)
    timeoutDuration = get_timeout_duration(parent)

    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Record file"\n'
    pascal_code += depth2tab(depth) + 'rec "%s" %s -keys %s %s\n' % (parent.data.filename, timeoutDuration, stopOnDtmf, continueAfterHangup)
    pascal_code += make_pascal(parent.child, depth + 1)
    pascal_code += depth2tab(depth-1) + '}\n'

    return pascal_code

def make_menu_pascal_code(parent, depth):
    length = len(parent.items)
    pascal_code = depth2tab(depth-1) + "{\n"
    pascal_code += depth2tab(depth) + '!"Menu"\n'
    pascal_code += depth2tab(depth) + 'nvd_brk_%s = 0\n' % length
    pascal_code += depth2tab(depth) + 'nvd_loop%s = 0\n' % length


    pascal_code += depth2tab(depth) + 'while nvd_loop%s < %s' % (length, length) + ' and nvd_brk_%s=0\n' % length
     
    for index, children in enumerate(parent.items):
        if children.condition == 'else':
            pascal_code += depth2tab(depth + 1) + 'else\n'
        else:
            pascal_code += depth2tab(depth + 1) + 'if Key = "%s"\n' % str(children.condition)
        pascal_code += make_pascal(children.branch, depth + 2)
    
    pascal_code += make_pascal(parent.child, depth + 1) 
    pascal_code += depth2tab(depth-1) + '}\n'
    
    return pascal_code

def make_pascal(children, depth):
    pascal_code = ""
    if is_repeat(children):
        pascal_code += make_repeat_pascal_code(children, depth)
    elif is_play(children):
        pascal_code += make_play_pascal_code(children, depth)
    elif is_record(children):
        pascal_code += make_record_pascal_code(children, depth)
    elif is_getKey(children):
        pascal_code += make_getKey_pascal_code(children, depth)
    elif is_menu(children):
        pascal_code += make_menu_pascal_code(children, depth)
    elif is_sequence(children):
        pascal_code += make_sequence_pascal_code(children, depth)
    elif is_return(children):
        pascal_code += make_return_pascal_code(children, depth)
    elif is_case(children):
        pascal_code += make_case_pascal_code(children, depth)
    elif is_hangup(children):
        pascal_code += make_hangup_pascal_code(children, depth)
    elif is_dial(children):
        pascal_code += make_dial_pascal_code(children, depth)
    elif is_testIF(children):
        pascal_code += make_testIF_pascal_code(children, depth)
    return pascal_code

def find_children(obj, pascal_code, depth):
    global pascal
    pascal_code += make_pascal(obj.child, depth)
    pascal = pascal_code

find_children(json_object, "", 1)

print pascal
