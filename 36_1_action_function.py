def write_log(message):
    with open('log.txt', 'a') as file:
        file.write(message + '\n')


# write_log("Starting the program")
# write_log("User logged in")
write_log("App stopped")
