import os
from glob import glob
from lib.score import score

scraped_root_directory="www_roots"

def cls():
    os.system('clear')

def search():
    s = raw_input("Type your search query:")
    #TODO call indexer for searching

def get_all_departments(root_path):
    return [x[1] for x in os.walk(root_path)][0]

def get_all_txt_files_in(path):
    """Returns all text files in all folders and sub-folders found"""
    return [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.txt'))]

def get_score(data):
    """Get score for file"""
    return score(data)

def get_text_from(file_path):
    """Retrieve text from file"""
    with open(file_path, 'r') as file:
        return file.read()

def get_department_score(department):
    """Gets the total score for that department"""
    path = scraped_root_directory + "/" + department
    score = 0
    all_files = get_all_txt_files_in(path)
    if len(all_files) == 0:
        return 0

    for file_path in all_files:
        file_content = get_text_from(file_path)
        score = score + get_score(file_content)
    return score / len(all_files)

def classifier(score):
    """Return Positive, Negative or Neutral"""
    #TODO: This will need to be changed depending on what kind of scoring is returned.....
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"

def compare_positivity(department_a, department_b):
    score_a = get_department_score(department_a)
    score_b = get_department_score(department_b)

    if score_a > score_b:
        print department_a, "is more positive than", department_b
    elif score_a < score_b:
        print department_b, "is more positive than", department_a
    else:
        print "Both department:", department_a, "and", department_b, "have same positivity score"

def scrap_new_link():
    """Add a new Department"""
    link = raw_input("Please enter the root link for Department:")
    print "Scraping all within link....."
    #TODO call Scraper to retrieve new link

def get_departments_with_score_classifier():
    d = {}
    for x in get_all_departments(scraped_root_directory):
        s = get_department_score(x)
        c = classifier(s)
        d[x] = (s, c)

    sorted_keys = sorted(d, key=lambda score: score[0], reverse=True) #TODO: Currently set highest value as most positive. VERIFIY that is true
    return d, sorted_keys

def print_departments_score_classifier():
    d, sorted_keys = get_departments_with_score_classifier()
    print
    print d
    for name in sorted_keys:
        print name
        print "\tscore:", d[name][0]
        print "\tclassifier:", d[name][1]
    print

def get_most_positive():
    d, sorted_keys = get_departments_with_score_classifier()
    return sorted_keys[0], d[sorted_keys[0]]

def get_most_negative():
    d, sorted_keys = get_departments_with_score_classifier()
    last_element = sorted_keys[len(sorted_keys)-1]
    return last_element, d[last_element]

def get_dep_choice():
    deps = get_all_departments(scraped_root_directory)
    while True:
        print "Departments:"
        for x in range(0, len(deps)):
            print x, ":", deps[x]
        user_choice = int(raw_input("Please select the correct number:"))
        if user_choice >= 0 and user_choice < len(deps):
            return deps[user_choice]

def print_score_classifier_for(department):
    """Print score, classifier for each scrapped link in department"""
    path = scraped_root_directory + "/" + department
    d = {}
    for file_path in get_all_txt_files_in(path):
        file_content = get_text_from(file_path)
        score = get_score(file_content)
        title = file_path #TODO: maybe change to h1 title for that article
        d[title] = score

    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

    for x in sorted_d:
        name = x[0].split("/")[2].split(".")[0]
        score = x[1]
        print name
        print "\tscore:", score
