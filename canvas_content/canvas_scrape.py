import os
import sys

from pathlib import Path
from canvasapi import Canvas

import config as config

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

    def get_user_details(self, id_type=None, **kwargs):
        return super().get_user(self.user_id, id_type, **kwargs)

    def get_course_details(self, course_id = ''):
        '''
        Get course details of a particular course of the user - 
            - Credits
            - Grades
        '''
        user = self.get_user(self.user_id)
        pass

    def get_user_course_details(self):
        '''
        Get all course details of the user - 
            - Credits
            - Grades
        '''
        user = self.get_user(self.user_id)
        courses = user.get_courses()

        courses_dict = {}
        for course in courses:
            courses_dict[course.name]= (course.id, course.course_code)

        return courses_dict


    def get_course_files(self, course_id = ''):
        '''
        Get the course files of a specific course into the required location
        Current file types supported - 
            pdf
        '''
        if course_id == '':
            return
        
        course_obj = self.get_course(course_id)
        course_sf = ''.join([token[0].upper() for token in course_obj.name.split() if token[0].isalpha()])

        # Get the file location of the user
        package_loc = os.path.dirname(__file__)
        file_dir_loc = os.path.join(package_loc,'files')

        course_file_loc = os.path.join(file_dir_loc,course_sf)
        try:
            os.mkdir(course_file_loc)
        except FileExistsError:
            print("Directory for particular course already exists")

        files = course_obj.get_files()

        # Download the files 
        # try:
        files_allowed = list(config.file_types.values())[0]
        for file in files:
            if files_allowed in str(file):
                file_download_loc = os.path.join(course_file_loc, str(file))
                file.download(file_download_loc)
        # except Exception as e:
        #     return f"Exception accessing files - {e}"
        
        return f"Files downloaded successfully"


    def get_user_course_files(self):
        '''
        Get course files of all courses user is enrolled in into the required location
        Current file types supported - 
            pdf
        '''
        course_dict = self.get_user_course_details()
        # Get the courses for the user
        package_loc = os.path.dirname(__file__)
        file_dir_loc = os.path.join(package_loc,'files')

        for key, value in course_dict.items():
            print(f'Getting course files for course - {key}')
            try:
                ret = self.get_course_files(value[0])
                print(f'{key} - {ret}')
            except Exception as e:
                print(f"{key} - Exception raised - {e}")
            





if __name__ == '__main__':


    canvas_obj = CanvasScraper(api_url=config.CANVAS_API_URL, 
                               api_key=config.CANVAS_API_KEY, 
                               user_id=config.CANVAS_USER_ID)

    user = canvas_obj.get_user_details()
    print('User',user)

    print(canvas_obj.get_user_course_details())

    canvas_obj.get_user_course_files()


    # Course details


    




