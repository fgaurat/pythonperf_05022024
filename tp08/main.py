from UserDAO import UserDAO



def filter_male(gen):
    for u in gen:
        if u.gender == "Male":
            yield u

def main():
    # dao = UserDAO('tp08/users_db.db')

    with UserDAO('tp08/users_db.db') as dao:

            # iter = dao.findAll()
            # users = list(iter)
            user = dao.findById(2001)
            # for m in filter_male(dao.findAll()):
            #     print(m)


            # # history | grep python

            # for user in iter:
            #     if user.gender == "Male":
            #         print(user)

            # user = next(i)
            # print(user)
            # user = next(i)
            # print(user)


            # for user in dao.findAll():
            #     print(user)

            # for user in users:
            #     print(user.last_name)

if __name__=='__main__':
    main()
