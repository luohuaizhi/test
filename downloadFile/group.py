import os

SRCPATH = 'r"G:\yunsign_contract"'
DSTPATH = r"G:\contracts"
CPCMD = "robocopy {src_path} {dst_path} {file}"
PER = 3601


def main():
    print os.path.abspath(os.getcwd())
    file_list = os.listdir(SRCPATH)
    file_num = len(file_list)
    # create dir
    for i in xrange(7):
        if (i+1)*PER > file_num:
            break
        for j in xrange(4):
            # os.makedirs('dir'+str(i)+str(j))
            dirname = 'dir'+str(i)+str(j)
            dst_path = os.path.join(DSTPATH, dirname)
            for f in xrange(PER):
                cmd = CPCMD.format(SRCPATH, dst_path, file_list[f])
                print cmd
                # os.system(cmd)

    print "end"


if __name__ == '__main__':
    # os.chdir(r"G:\contracts")
    main()
