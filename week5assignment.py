from abc import ABC, abstractmethod

class Criterion(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def judge(self, value):
        ...
    def evaluate(self,value):
        result=self.judge(value)
        if result:
            status="PASS"
        else:
            status="FAIL"
        print(f"[{status}] {self.name}: {value}")
        return result
class MinWordsCriterion(Criterion):
    def __init__(self,min_words):
        name=f"MinWords({min_words})"
        super().__init__(name)
        self.min_words=min_words
    def judge(self,value):
            count=len(value.split())
            result= count >= self.min_words
            return result
    
class MaxLengthCriterion(Criterion):
    def __init__(self,max_len):
        name=f"MaxLength({max_len})"
        super().__init__(name)
        self.max_len=max_len

    def judge(self,value):
        result= len(value) <=self.max_len
        return result
            
class NoBannedWordsCriterion(Criterion):
    def __init__(self,banned):
        self.banned=banned
        name="NoBannedWords"
        super().__init__(name)
    def judge(self,value):
        for word in self.banned:
            if word in value.lower():
                result=False
                return result
        result=True
        return result
        
class EndsWithPunctuationCriterion(Criterion):
    def __init__(self):
        name = "EndsWithPunctuation"
        super().__init__(name)

    def judge(self, value):
        if len(value) > 0 and (value[-1] == "." or value[-1] == "!" or value[-1] == "?"):
            result = True
        else:
            result = False
        return result
    
class ModerationReport:
    def __init__(self):
        self.inputs=[]
    def add(self,criterion_name,value,passed):
        result=(criterion_name,value,passed)
        self.inputs.append(result)
        return result
    
    def summary(self):
        total = len(self.inputs)
        passed_count = 0
        failed_count = 0

        for name, value, passed in self.inputs:
            if passed:
                passed_count += 1
            else:
                failed_count += 1

        print(f"Total: {total}, Passed: {passed_count}, Failed: {failed_count}")

        result = (total, passed_count, failed_count)
        return result

class ReviewField:
    def __init__(self,field_name):
        self.field_name=field_name
        self.criteria=[]
        self.report=ModerationReport()

    def add_criterion(self,criterion):
        self.criteria.append(criterion)
        result=criterion
        return result
        
    def moderate(self,value):
        print(f'Moderating {self.field_name}: "{value}"')
        overall=True

        for criterion in self.criteria:
            result=criterion.evaluate(value)
            self.report.add(criterion.name,value,result)
            if not result:
                overall=False

        result=overall
        return result
        
    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        result=self.report.summary()
        return result
    
review = ReviewField('comment')
review.add_criterion(MinWordsCriterion(3))
review.add_criterion(MaxLengthCriterion(50))
review.add_criterion(NoBannedWordsCriterion(['spam', 'fake']))
review.add_criterion(EndsWithPunctuationCriterion())

valid1 = review.moderate('Great product overall!')
print(f'Valid: {valid1}')
print()

valid2 = review.moderate('ok')
print(f'Valid: {valid2}')
print()

valid3 = review.moderate('This is spam content')
print(f'Valid: {valid3}')
print()

review.show_report()

try:
    c = Criterion('test')
except TypeError:
    print('Cannot instantiate abstract class')

         
        






        

