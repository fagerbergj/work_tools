#
#@autor: Jason Fagerberg
#@date: January 15 2018
#@params: rr string containing '~', space deliminated list of params
#@output: if each arg is in rr string
#@assumptions: '//' ends rr string, you are looking for a specific number in a string
#             Num of time a specific number is input <= number of occurances in rr
#

#checks to see if a string is numeric
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#find all index values       
def find(s, t):
  c = s
  res = []
  amt_cut = 0
  for i in range(s.count(t)):
    res.append(c.find(t) + amt_cut)
    amt_cut = c.find(t) + len(t)
    c = c[c.find(t) + len(t):]
  return res

#checks to see if number is exactly included within a string
def exact(r, p):
  back = False
  front = False
  res = find(r, p) 

  if(len(p) > len(r)):
    return False

  for i in res:
    if(i + len(p) <= len(r) and not is_number(r[i+len(p)])):
      back = True
    if(i-1 >= -1 and not is_number(r[i-1])):
      front = True
  return front and back
  

#take input until '//' is typed
def main():
  print("input rawread, when finished type '//': ")
  rr = ""
  while rr[len(rr)-3:len(rr)-1] != "//":
    rr += input() + "\n"

  #take params into dynamic array
  print("input parameters separated by a space: ")
  args = input().split()

  #loop through args check exact match
  for n in args:
    if(rr.count(n) >= args.count(n) and exact(rr,n)):
      print(n + " contained: PASS")
    else:
      print(n + " contained: FAILED")

if __name__=="__main__": main()