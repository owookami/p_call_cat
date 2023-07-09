from django.db import models

# Create your models here.
class Company(models.Model):
    rowNum = models.TextField() #번호
    opnSfTeamCode = models.TextField() #개방자치단체코드
    mgtNo = models.TextField() #관리번호
    opnSvcId = models.TextField() #개방서비스ID
    updateGbn = models.TextField() #데이터갱신구분
    updateDt = models.TextField() #데이터갱신일자
    opnSvcNm = models.TextField() #개방서비스명
    bplcNm = models.TextField() #사업장명
    sitePostNo = models.TextField() #지번우편번호
    siteWhlAddr = models.TextField() #지번주소
    rdnPostNo = models.TextField() #도로명우편번호
    rdnWhlAddr = models.TextField() #도로명주소
    siteArea = models.TextField() #소재지면적
    apvPermYmd = models.TextField() #인허가일자
    apvCancelYmd = models.TextField() #인허가취소일자
    dcbYmd = models.TextField() #폐업일자
    clgStdt = models.TextField() #휴업시작일자
    clgEnddt = models.TextField() #휴업종료일자
    ropnYmd = models.TextField() #재개업일자
    trdStateGbn = models.TextField() #영업상태코드
    dtlStateGbn = models.TextField() #상세영업상태코드
    dtlStateNm = models.TextField() #상세영업상태명
    x = models.TextField() #좌표정보(X)
    y = models.TextField() #좌표정보(Y)
    lastModTs = models.TextField() #최종수정일자
    uptaeNm = models.TextField() #업태구분명
    siteTel = models.TextField() #전화번호
