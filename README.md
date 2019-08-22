# Reaper Revision Parser
Script allows you to parse strings which contain timestamp and comments and convert them into Reaper markers.
I created it to optimize my workflow, when i have to go over revisions for a project.
I thought that i would rather do everything inside Reaper and don't switch to external windows/emails to check with revisions.

# How it works
The script parses the input string and converts each line into timestamp and comment and generates a marker with comment as it's name. If timestamp contains more than one value, i.e in and out, the script generates a region instead.

# TO-DO
1. Add removal of existing markers.
