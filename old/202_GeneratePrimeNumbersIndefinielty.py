"""
Prime number generator
"""

def generate_prime(N):
    prime_numbers=[2,3,5]
    if N<=5:
        return list(filter(lambda x: x<=N,prime_numbers))
    else:
        number=6
        print(number)
        while number<=N:
            if any(list(map(lambda x: number%x==0,prime_numbers))):
                number +=1
                continue
            else:
                prime_numbers.append(number)
                number +=1

            

    return prime_numbers


if __name__ == "__main__":
    print(generate_prime(3))
