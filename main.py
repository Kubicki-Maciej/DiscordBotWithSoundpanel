import gui
import concurrent.futures
import bot

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(gui.run)
        executor.submit(bot.run)
