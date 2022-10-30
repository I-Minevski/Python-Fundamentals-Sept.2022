is_balanced=True
lines=int(input())
is_open=False
parenth=False
for i in range(lines):
    char=input()
    if char=="(":
        is_open=True
        parenth=True
    if is_open==True:
        if char==")":
            is_open=False
            parenth=True
    elif char==")":
        is_balanced=False
if parenth==False:
    is_balanced=False
if is_open==True:
    is_balanced=False
if is_balanced==True:
    print("BALANCED")
else:
    print("UNBALANCED")