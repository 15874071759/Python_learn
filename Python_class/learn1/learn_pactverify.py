from pactverify.matchers import Matcher, EachLike, PactVerify
from models.bankcards.withdraw_cards import WithdrawCardsClient
import json
"""
1.Matcher类：值匹配
2.Like类：类型匹配
3.EachLike类：数组类型匹配
4.Term类：正则匹配
5.Enum类：枚举匹配
复杂规则匹配：
{{}} Like匹配
[[]] EachLike匹配
{[]} Like('code':0,'data':EachLike({'id':1}))

文档地址：https://pypi.org/project/pactverify/
"""
# 定义契约格式
expect_format = Matcher({
    'code': 0,  # code key存在,值相等,code==0
    'message': 'success',  # msg key存在,值相等,msg=='success'
    # [{}]结构
    'data': Matcher({
        'list': EachLike({
            "id": "465",
            "bank_id": "14",
            "name": "member9号",
            "account": "88889",
            "swift_code": "UOVBSGSG",
            "account_type": "SGD",
            "country": "SINGAPORE",
            "address": "",
            "remark": "测ttt",
            "region": "SINGAPORE",
            "bank": "United Overseas Bank Limited",
            "icon": "https://cdn-support.lbkrs.com/uploads/files/201911/BsVEPetG3Uy1nQmAbuDQ9aKCsmhct7gj.png",
            "bank_en": "UOB Bank",
            "region_name": "新加坡银行",
            "name_en": "heha",
            "bank_code": ""
        }, nullable=True)
    })
})
# hard_mode默认为true,hard_mode = True时,实际返回key必须严格等于预期key;hard_mode = False时,实际返回key包含预期key即可
mPactVerify = PactVerify(expect_format, hard_mode=True)
temp = WithdrawCardsClient()
payload = {'withdraw': 0}
res = temp.query_withdraw_cards(payload)
# 校验实际返回数据
mPactVerify.verify(res.json())
# 校验结果  False
print(mPactVerify.verify_result)
print(mPactVerify.verify_info)

#断言匹配结果，如果verify_result结果为false,则打印verify_info错误信息
assert mPactVerify.verify_result, json.dumps(mPactVerify.verify_info)




