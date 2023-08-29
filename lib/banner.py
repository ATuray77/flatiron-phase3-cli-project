from prettycli import green, yellow

class Banner:
    def welcome(self):
        print(yellow("Welcome to"))
        print(green
              (
            """
        
___       __           .  __      __        __               __      __        __        __   ___ 
 |  |  | |__)  /\  \ / ' /__`    |__)  /\  |__) |__/ | |\ | / _`    / _`  /\  |__)  /\  / _` |__  
 |  \__/ |  \ /~~\  |    .__/    |    /~~\ |  \ |  \ | | \| \__>    \__> /~~\ |  \ /~~\ \__> |___ 
                                                                                                  
    
                                                                                                                                                                                                                                                            

             """
              ).bold()
              )