import csv

FILE_NAME = "movie_ratingcsv"

def load(soubor):
    '''
    :param soubor: načtený csv soubor s daty o filmu
    :return: načtená data s daným hodnocením, které spouštíme v hlavní funkci
    '''

    with open("movie_rating.csv") as file_name:
        movie_rating = csv.reader(file_name, delimiter=';', quotechar='|')

        movies_data = []
        for row in movie_rating:
            movie = []
            for j in row[:2]:
                movie.append(j)
                score = []
            # movies_data.append(movie)
            for i in row[2:]:
                if i != 'x':
                    score.append(i)
            movie.insert(2, score)
            movies_data.append(movie)

    print(movies_data)
    # return movies_data

def main():
    '''
    :return: vracíme načtená data s údaji o hodnocení filmů
    '''
    x = load(FILE_NAME)

if __name__ == '__main__':
    main()
