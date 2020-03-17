import os

def main():
    try:
        # open the names.txt file in read mode.
        infile=open("servers.txt", "r")

        # set an accumulator for number of names
        numbers_of_servers=0.0

        # read the first line
        line=infile.readline()

        # read the rest of the file
        while line!="":
            #print("knife ssh 'name:"+line.strip()+ "' 'sudo chef-client' -x USERNAME -P PASSWORD")
            command = "knife ssh 'name:"+line.strip()+ "' 'sudo chef-client -o recipe['chrony_conf']' -x root -P blue23vasthav"
            os.system(command)
            #print(command)
            numbers_of_servers+=1
            line=infile.readline()

        # print the numbers of names in the names.txt file.
        print("There are", int(numbers_of_servers), "servers in total.")

        # close the file
        infile.close()
    except IOError as err:
        print (err)

# call the main function
main()
