a = ['09-12-2024', '10-12-2022', '18-10-2023', '10-12-2024']


def f(a):
    return (a[6:], a[3:5], a[:2])

print(sorted(a, key=f))
