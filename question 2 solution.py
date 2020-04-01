def fun(nestedDict, Dic, currentKey):
    for key in nestedDict,key():
        if type(nestedDict[key])==int:
            Dic[(currentKey+"."+key).strip(".")]=nestedDict[key]
        else:
            dic=fun(nestedDict[key],Dic,(currentKey+"."+key).strip("."))
    return Dic
def func_dic(nestedDic):
    return fun(nestedDic,dic(),"")
def main():
    nestedDictionary= {
        "key":3,
        "foo": {
            "a": 5,
            "bar": (
                "bar":8
            }
        }
    }

    dicten=func_dic(nestedDictionary)
    print(dicten)
if__name__==,"__main__":
    main()

                

   
            
