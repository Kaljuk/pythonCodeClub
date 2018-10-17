def sort_file(contents, **a):
    instep = a.get('instep')  or ','
    inend  = a.get('onend')   or '\n'
    outstep= a.get('outstep') or instep
    outend = a.get('outend')  or inend
    
    lines = sorted(contents.split('\n'))
    lines = list(filter(lambda l: (len(l.strip())>0 and l.strip()[0] != "#"), lines))
    lines = [line.replace(instep, outstep) for line in lines]
    lines = (outend).join(lines)
    return repr(lines)


# contents = "2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a"

# compareTo= "1,4,d\n2,3,d\n2,4,a\n2,4,x\n8,2,z"
# print(sort_file(contents))
# print("Compare to: ", repr(compareTo))

# compareTo="1:4:d -- end\n2:3:d -- end\n2:4:a -- end\n2:4:x -- end\n8:2:z"
# print(sort_file(contents, outstep=':', outend=' -- end\n'))
# print("Compare to: ", repr(compareTo))


# contents = "2,3,d.#.1,4,d"
# compareTo= "1,4,d.2,3,d"
# print(sort_file(contents, inend='.'))
# print("Compare to: ", repr(compareTo))


#print(sort_file(contents))
#print(compareTo)
