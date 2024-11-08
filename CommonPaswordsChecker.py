def check_password(password:str):
    flag : bool =  False
    with open('sample.text','r') as file:
        common_passwords: list[str] = file.read().splitlines()
        print(common_passwords)
    for i, common_password in enumerate(common_passwords, start =1):
        if password == common_password:
            print(f"{password} is already used by too many people is the  ({i}) th most hackeable word")
            flag = True
    if flag:
        pass
    else :
        if len(password) != 0:
            return
        print("Not so fast smarty pants, you cannot leave this empty try again")


def main():
    check_password("sfhdsdhs iuvwrey tpwe48564w953945  sd")
if __name__ == '__main__':
    main()
