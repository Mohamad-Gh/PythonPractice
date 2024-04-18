
def main():
    dict = {"name":"harry, potter","house":"glyfendor"}
    print(split(dict))

def split(each):
    out_list = {}
    name, last = each["name"].split(", ")
    out_list["name"] = name
    out_list["last"] = last
    out_list["house"] = each["house"]
    return out_list

main()