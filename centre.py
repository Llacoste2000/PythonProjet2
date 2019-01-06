import menu
import pickle

def run_this():

    menu.run()
    with open('score.pkl', 'wb') as scoreFile:
        pickle.dump([0, 0, 0, 0], scoreFile)
    print(1)

def main():

    run_this()

if __name__ == "__main__":
   main()