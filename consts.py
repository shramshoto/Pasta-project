BACKGROUND_COLOR=(255,230,247)
WINDOW_WIDTH=1000
WINDOW_HEIGHT=500
import pygame

KITCHEN_IMG=pygame.image.load('kitchen.png')
KITCHEN_SIZE=(WINDOW_WIDTH,WINDOW_HEIGHT)
SAUCE_IMG=pygame.image.load('tomato sauce GIF.gif')

TOMATO_IMG=pygame.image.load('tomato sauce GIF.gif')
TOMATO_WIDTH=350
TOMATO_HEIGHT=130
TOMATO_SIZE=(TOMATO_WIDTH,TOMATO_HEIGHT)
TOMATO_INITIAL_X=465
TOMATO_INITIAL_Y=160
TOMATO_START_LOCATION=TOMATO_INITIAL_X, TOMATO_INITIAL_Y

'''PASTA_IMG=pygame.image.load("pasta.png")
PASTA_RECT=PASTA_IMG.get_rect()
PASTA_WIDTH = 150
PASTA_HEIGHT = 60
PASTA_SIZE=(PASTA_WIDTH, PASTA_HEIGHT)
PASTA_INITIAL_X = 850
PASTA_INITIAL_Y = 100
PASTA_START_LOCATION=PASTA_INITIAL_X, PASTA_INITIAL_Y

POT_IMG=pygame.image.load('pot1.png')
POT_RECT=POT_IMG.get_rect()
POT_WIDTH = 300
POT_HEIGHT = 250
POT_SIZE= POT_WIDTH, POT_HEIGHT
POT_INITIAL_X = 500
POT_INITIAL_Y = 180
POT_START_LOCATION=POT_INITIAL_X, POT_INITIAL_Y

PAN_IMG=pygame.image.load('pan.png')
PAN_RECT=PAN_IMG.get_rect()
PAN_WIDTH=250
PAN_HEIGHT=200
PAN_SIZE=(PAN_WIDTH, PAN_HEIGHT)
PAN_INITIAL_X=800
PAN_INITIAL_Y=180
PAN_START_LOCATION=PAN_INITIAL_X, PAN_INITIAL_Y

STOVE_IMG=pygame.image.load('stove.png')
STOVE_RECT=STOVE_IMG.get_rect()
STOVE_WIDTH=150
STOVE_HEIGHT=100
STOVE_SIZE=(STOVE_WIDTH, STOVE_HEIGHT)
STOVE_INITIAL_X1 = 800
STOVE_INITIAL_Y1 = 400
STOVE_START_LOCATION=STOVE_INITIAL_X1, STOVE_INITIAL_Y1

STOVE_INITIAL_X2 = 500
STOVE_INITIAL_Y2 = 100
STOVE_START_LOCATION1=STOVE_INITIAL_X2, STOVE_INITIAL_Y2'''


FONT_NAME = "Calibri"
MESSAGE_A =  "אמולסיה (Emulsion) היא תערובת יציבה בין שני נוזלים שאינם מתערבבים באופן טבעי – כמו שמן ומים.\n רטבים אמולסיביים כמו אליו אה אוליו, פסטו וקרבונרה לרוב כוללים בתוכם גורם מחבר (מתחלב) כמו יין, ביצה, לימון או חומץ ומסתמכים עליהם ללכוד את השמן ולחבר בינו לבין השאר."

MESSAGE_B = "אם הרוטב מכיל מעל 18% שמן *ללא* מתחלבים, הוא ייפרד אלא אם כן פני הפסטה יספקו מספיק מקומות עיגון. לדוגמה - הרוטב שלנו, רוטב עגבניות.\n ומה שמספק את מקומות העיגון האלו לרוטב העגבניות הוא העמילן שעל פני הפסטה וגם במים בהם בישלו אותה. חשוב לשמור עליו בזמן הבישול אחרת הרוטב לא יידבק וישחה בצלחת אחרי שכבר סיימתם לאכול."
MESSAGE_C = " כשהעמילן פוגש בשמן הוא לוכד אותו במולקולות שלו מה שמוריד את אחוזי השומן של הרוטב. במים חמים, מבנה העמילן נשבר ומאפשר לו ליצור קשרי מימן עם המים - מה שיוצר מן ג'ל המשמש כדבק.\n השטיפה של הפסטה במים קרים לא רק שוטפת את העמילן שעל שטח הפנים של הפסטה ועלולה להפחית את ייווצרות הקשרים בין המים לעמילן, אלה גם מקררת אותה עד פחות מ-60°C, הטמפרטורה בה האמולסיה של הרוטב מתחילה להישבר - השמן נפרד מהמים בחזרה.\n לכן רצוי לשמור כחצי כוס מהמים שבהם הפסטה בושלה, להוסיף אותה בדירוג אל הרוטב, ולא לשטוף את הפסטה במים קרים בשום אופן."
MESSAGE_RECIPE = "מצרכים:\n פסטה,\n מים,\n מלח,\n לרוטב:\n עגבניות מרוסקות,\n פלפל,\n בזיליקום,\n שום,\n פלפל שחור.\n הוראות:\n העבר מהמים בהם בושלו הפסטה לרוטב"

FONT_SIZE_SMALL = int(0.02 * 500)
FONT_SIZE = int(0.05 * 500)

FONT_LOCATION = (970, 70)
FONT_LOCATION_RECIPE = (1000, 0)

COLOR = (255, 255, 255)


'''SPOON = {"width": image.get_width()*0.5, "height": image.get_height()*0.5, "obj_x":,"obj_y":,
"animations": [Screen1.animate_scoop(), Screen1.spoon_move(), Screen1.spoon_pour()]}
appearance = [SPOON]'''