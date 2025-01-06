from canvas_content.canvas_scrape import CanvasScraper
import config as config


if __name__ == '__main__':

    canvas_obj = CanvasScraper(api_url=config.CANVAS_API_URL, 
                               api_key=config.CANVAS_API_KEY, 
                               user_id=config.CANVAS_USER_ID)

    user = canvas_obj.get_user_details()
    
    print('User',user)
    print(canvas_obj.get_user_course_details())

    canvas_obj.get_user_course_files()

    

