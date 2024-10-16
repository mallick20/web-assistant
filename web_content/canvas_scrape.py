import os
import sys

from pathlib import Path

from canvasapi import Canvas

# Canvas API URL
API_URL = "https://rutgers.instructure.com"
# Canvas API key
API_KEY = "6948~WRFHTfT4nx2u9yN9HeEKLnNzX33DrJWNRvvNTRvmT8r4PJB3XD94GTLtFQweT4fU"
# API_KEY = "6948~mxNHRC2fnZ7CBrwkak4XBNRfXZunX7kHUUrYhRRVN4GvyGGWwt7cfK8AT8CzcFFG"
USER_ID = "593172"

class CanvasScraper(Canvas):
    '''
    Represents the Canvas scrape object

    assignment - Get user assignments
    quiz - Get user quizzes
    course - Get course details and materials
    
    '''

    def __init__(self, api_url = '', api_key = '', user_id = ''):
        self.API_URL = api_url
        self.API_KEY = api_key
        self.user_id = user_id
        super().__init__(self.API_URL, self.API_KEY)

    def get_user(self, user, id_type=None, **kwargs):
        return super().get_user(user, id_type, **kwargs)

    def get_course_details(self, course_id = ''):
        pass





if __name__ == '__main__':

    canvas_obj = CanvasScraper(api_url=API_URL, api_key=API_KEY, user_id=USER_ID)

    user = canvas_obj.get_user(USER_ID)
    print('User',user)

    # Get the courses for the user
    package_loc = os.path.dirname(__file__)
    file_dir_loc = os.path.join(package_loc,'files')

    try:
        os.mkdir(file_dir_loc)
    except FileExistsError:
        print("Directory for course files already exists")
    courses = user.get_courses()
    for course in courses:
            print('***', course.name,'->', course.id,'->', course.course_code)
            course_sf = ''.join([token[0].upper() for token in course.name.split() if token[0].isalpha()])

            file_loc = os.path.join(file_dir_loc,course_sf)
            print(file_loc)
            # Make directory for the course
            try:
                os.mkdir(file_loc)
            except FileExistsError:
                print("Directory for particular course already exists")


            files = course.get_files()

            # First store the files at the location
            with open(os.path.join(file_loc, 'files_list.txt'),'w') as f:
                for file in files:
                    f.write(f'{str(file)}\n')


    # Course details

    




