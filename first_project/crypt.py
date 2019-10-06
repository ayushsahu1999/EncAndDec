import string

def decode(s):
    s = str(s)
    st = '00000000'
    ans = ''
    st = ''
    dec, decimal, num = 0, 0, 0
    ch = ''
    ans = ''
    i = 0

    while(i < len(s)):
        if (s[i] == '('):
            st = '00000000'

        elif (s[i] == ')'):
            st = int(st)
            num = 0
            decimal = 0
            dec = 0
            while (st != 0):
                dec = st % 10
                decimal = decimal + dec * pow(2, num)
                st = st // 10
                num+=1

            ch = chr(decimal)
            ans = ans + str(ch)

        else:
            st = list(st)
            n = s[i]
            st[7-int(n)] = '1'
            st = ''.join(st)


        i+=1

    return ans


def encode(s):
    i = 0
    num = ''
    ans = ''
    while (i < len(s)):
        n = ord(s[i])
        ch = ''


        z = 0
        zero = ''
        num = bin(n).replace("0b", "")
        if (len(num) < 8):
            z = 8-len(num)
            while (z > 0):
                zero = zero + '0'
                z-=1

        j = 0

        num = zero + num

        while (j < len(num)):
            if (num[j] == '1'):

                ch = ch + str(7-j)

            j+=1

        ch = ''.join(reversed(ch))


        ans = ans + '(' + ch + ')'
        i+=1

    return ans

# 
# a = input('Enter 1 for decode\nEnter 2 for encode')
# print (a)
#
# if (a == '1'):
#     q = str(input('Enter the String like (125)(458) = '))
#
#     decode(q)
#
# elif (a == '2'):
#     t = input('Enter the String like ABCS = ')
#     encode(t.upper())
#
# else:
#     print ('Wrong choice!')
