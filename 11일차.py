class BignumError(Exception):
    def __init__(self, msg):
        self.msg=msg

    def __str__(self):
        return self.msg

try:
    print("한자리 전용 나누기 앱입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자 : ")))
    nums.append(int(input("두번째 숫자 : ")))
    nums.append(int(nums[0]/nums[1]))
    if nums[0]>= 10 or nums [1] >= 10:
        raise BignumError("입력값 {0}, {1}".format(nums[0],nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:    
    print("올바른 input이 아닙니다.")
except ZeroDivisionError as err:
    print(err)
except BignumError as err:
    print("올바른 input이 아닙니다. 한 자리 수만 입력하세요.")
    print(err)
except Exception as err:
    print("알 수 없는 오류가 발생했습니다. 피드백해주시면 빠른 시일내에 고치겠습니다.")
    print(err)
finally:
    print("앱을 이용해주셔서 감사합니다. 앱에 대한 평가를 통해 더욱 발전해 나가겠습니다.")