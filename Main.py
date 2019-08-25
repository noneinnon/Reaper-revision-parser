import reaper_python
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

proj = RPR_GetProjectName('', 0, 0)[1][:-4]

string = RPR_GetUserInputs('Revisions', 2, 'Enter revisions', '', 512)[4]
# RPR_ShowConsoleMsg(string)
if string:
    for index, line in enumerate(string.split('\n')):
        timestamp = re.findall(r'\d+.+\d+', line)[0]
        comment = re.split(r'\d+.+\d+', line, 1)[1]
        # RPR_ShowConsoleMsg(timestamp)
        timestamp = re.split(r'–|-|до', timestamp)
        # RPR_ShowConsoleMsg(timestamp)
        for i, each in enumerate(timestamp):
            timestr = each.replace('.', ':').strip()
            if len(timestr) < 6:
                timestr = '00:' + timestr + ':00'
            else:
                timestr = timestr + ':00'
            timestamp[i] = timestr
        start = RPR_parse_timestr_len(timestamp[0], 0, 5)
        try:
            end = RPR_parse_timestr_len(timestamp[1], 0, 5)
        except:
            end = 0
        isReg = False
        if end:
            isReg = True
        #RPR_ShowConsoleMsg([start, end, isReg, index])
        RPR_AddProjectMarker(proj, isReg, start, end, comment, index)
