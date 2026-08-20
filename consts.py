BACKGROUND_COLOR=(255,230,247)
WINDOW_WIDTH=1000
WINDOW_HEIGHT=500
import pygame
state = False

KITCHEN_IMG=pygame.image.load('kitchen.png')
KITCHEN_SIZE=(WINDOW_WIDTH,WINDOW_HEIGHT)
SAUCE_IMG=pygame.image.load('tomato sauce GIF.gif')

EMPTY_SPOON_IMG=pygame.image.load('pouring/pouring-1.png')
FULL_SPOON_IMG=pygame.image.load('pouring/pouring-5.png')
SPOON_WIDTH= EMPTY_SPOON_IMG.get_width()*0.1
SPOON_HEIGHT=EMPTY_SPOON_IMG.get_height()*0.1
SPOON_SIZE=(SPOON_WIDTH,SPOON_HEIGHT)
SPOON_INITIAL_X=400
SPOON_INITIAL_Y=150
SPOON_LOCATION=(SPOON_INITIAL_X,SPOON_INITIAL_Y)
SPOON_SECOND_X=500
SPOON_SECOND_Y=200

TOMATO_IMG=pygame.image.load('tomato sauce GIF.gif')
TOMATO_WIDTH=350
TOMATO_HEIGHT=130
TOMATO_SIZE=(TOMATO_WIDTH,TOMATO_HEIGHT)
TOMATO_INITIAL_X=465
TOMATO_INITIAL_Y=160
TOMATO_START_LOCATION=TOMATO_INITIAL_X, TOMATO_INITIAL_Y

FONT_NAME = "Solitreo"
MESSAGE_A =   "אמולסיה (Emulsion) היא תערובת יציבה בין שני נוזלים שאינם מתערבבים באופן טבעי – כמו שמן ומים.\n רטבים אמולסיביים כמו אליו אה אוליו, פסטו וקרבונרה לרוב כוללים בתוכם גורם מחבר (מתחלב)\n כמו יין, ביצה, לימון או חומץ ומסתמכים עליהם ללכוד את השמן ולחבר בינו לבין השאר."[::-1]

MESSAGE_B = "אם הרוטב מכיל מעל 18% שמן *ללא* מתחלבים, הוא ייפרד אלא אם כן פני הפסטה יספקו מספיק מקומות עיגון.\n לדוגמה - הרוטב שלנו, רוטב עגבניות.\n ומה שמספק את מקומות העיגון האלו לרוטב העגבניות הוא העמילן שעל פני הפסטה וגם במים בהם בישלו אותה.\n חשוב לשמור עליו בזמן הבישול אחרת הרוטב לא יידבק וישחה בצלחת אחרי שכבר סיימתם לאכול." [::-1]
MESSAGE_C = "כשהעמילן פוגש בשמן הוא לוכד אותו במולקולות שלו מה שמוריד את אחוזי השומן של הרוטב.\n במים חמים, מבנה העמילן נשבר ומאפשר לו ליצור קשרי מימן עם המים - מה שיוצר מן ג'ל המשמש כדבק.\n השטיפה של הפסטה במים קרים לא רק שוטפת את העמילן שעל שטח הפנים\n של הפסטה ועלולה להפחית את ייווצרות הקשרים בין המים לעמילן, אלה גם מקררת אותה עד פחות מ-60°C,\n הטמפרטורה בה האמולסיה של הרוטב מתחילה להישבר - השמן נפרד מהמים בחזרה.\n לכן רצוי לשמור כחצי כוס מהמים שבהם הפסטה בושלה, להוסיף אותה בדירוג אל הרוטב,\n ולא לשטוף את הפסטה במים קרים בשום אופן."[::-1]
MESSAGE_RECIPE = "מצרכים:\n פסטה,\n מים,\n מלח,\n לרוטב:\n עגבניות מרוסקות,\n פלפל,\n בזיליקום,\n שום,\n פלפל שחור.\n הוראות:\n העבר מהמים בהם בושלו הפסטה לרוטב"[::-1]

FONT_SIZE_SMALL = int(0.02 * 500)
FONT_SIZE = int(0.05 * 500)

FONT_LOCATION = (70, 70)
FONT_LOCATION_RECIPE = (910, 20)
COLOR = (0, 0, 0)


collage_img = pygame.image.load('collage.jpeg')
COLLAGE_SIZE = (6144*0.05, 1536*0.05)

