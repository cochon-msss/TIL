# HTML5 & CSS3

국비 부트캠프 HTML5 / CSS3 학습노트. 강의별 태그와 속성 예제를 정리했다.

## 강의 3. HTML 기본 태그 (h, p, br, hr, blockquote, pre)

- `h1`~`h6`: 제목 태그. 숫자가 커질수록 글자 크기가 줄어든다. 타이틀에 사용하며 볼드체로 표현된다.
- `p`: 단락. 본문에서 단락을 구분하거나 나타낼 때 사용하며 주로 글자를 담는다.
- `br`: 줄바꿈.
- `hr`: 수평선. 단락 구분이나 주제가 바뀔 때 사용한다.
- `blockquote`: 긴 인용문. 들여쓰기로 표현된다.
- `pre`: 공백이나 줄바꿈이 입력한 그대로 표현되는 태그.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <!--블럭형태의 글자 태그 >>> 박스처럼 작성한 순서대로 위에서 아래로 쌓이는 형태
  01. 제목태그
    h1~h6 : 숫자가 뒤로 갈수록 글자사이즈가 줄어듬, 타이틀에 사용, 볼드체

  <h1>header-1</h1>
  <h2>header-2</h2>
  <h3>header-3</h3>
  <h4>header-4</h4>
  <h5>header-5</h5>
  <h6>header-6</h6>-->

  <!--p:단락, 본문에서 단락을 구분하거나 나타낼 때 사용 주로 글자를 담아서 표현
  br: 줄바꿈 -->
  <h1>header -1</h1>
  <p>
    It is a long established fact that a reader will be distracted by the reada ble content of a page when looking <br/>
    at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as<br/>
    opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages <br/>
    and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites <br/>
    still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).<br/>
  </p>
  <p>
    It is a long established fact that a reader will be distracted by the readable content of a page when looking<br/>
    at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as <br/>
    opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages <br/>
    and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites <br/>
    still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).<br/>
  </p>

  <br/>
  <br/>
  <br/>

  <!--hr: 수평줄을 나타내는 태그 , 단락의 구분 주제가 바뀔 때 / 입체적-->
  <hr/>

  <br/>
  <br/>
  <br/>

  <!--인용문: 긴 인용문을 나타낼 때 사용하는 태그, 들여쓰기-->
  <h2>header -2</h2>
  <p>Why do we use it?</p>
  <blockquote>
    and more recently with desktop publishing software like Aldus
     PageMaker including versions of Lorem Ipsum.
  </blockquote>

  <br/>
  <br/>
  <br/>

  <!--공백이나 줄바꿈 등이 그대로 표현되어지는 태그-->
  <p>Why do we use it?</p>
  <pre>
    readable English. Many desktop publishing packages and web page editors
    now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will
    uncover many web sites        still in their infancy.
    Various versions have evolved over the years, sometimes by
  </pre>

</body>

</html>
```

## 강의 4. 글자를 꾸미는 인라인 태그와 특수문자

글자와 같은 성격(inline)을 가진 태그들.

- `strong`: 경고, 주의사항 등 중요한 내용 강조(볼드체). `b`: 단순히 글자를 굵게.
- `em`: 강조된 부분이나 저자의 생각(이탤릭체). `i`: 단순 이탤릭체.
- `q`: 짧은 인용(따옴표 표시). `blockquote`: 긴 인용(박스 성격).
- `mark`: 형광펜 효과(노란 배경).
- `span`: 글자를 꾸밀 때 사용하며 선택자와 함께 쓴다.
- `ruby` / `rp` / `rt`: 동아시아 글자의 발음 주석 표기.
- `del`: 취소선. `ins`: 밑줄.
- `sup`: 위첨자. `sub`: 아래첨자.
- 엔티티(entity): HTML에서 예약된 문자. 예) `&lt;` == `&#60;`(보다 작은), `&gt;` == `&#62;`(보다 큰), `&nbsp;` == `&#160;`(줄바꿈 없는 공백).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>글자와 같이 나열되는 태그</title>
</head>

<body>
    <h1>글자와 같은 성격을 가진 글자태그(inline)</h1>
    <!--<p>태그를 열고 닫으니 다음 단락으로 내려간다!</p>-->

    <h2>글자를 꾸며주는 태그들!</h2>
    <p>
      <!--볼드체로 표현-->
      <strong>경고,주의사항과 같이 중요한 내용들을 강조할 때!</strong><br/>
      <b>글자를 굵게 표현하고 싶을 때!</b>
   </p>
   <p>
    <!--이태릭체로 표현-->
    <em>주의 텍스트의 비해서 강조된 부분이나 저자의 생각 ~강조!</em><br>
    <i>이탤릭체를 표현하고 싶을 때</i>
   </p>

   <p>
    <!--인용표현-->
    <q>인용할 문구를 표현, 따옴표가 나타남! 글자와 같이 나열되어지며 짧은 부분의 인용을 표현할 때 사용</q>
   </p>
   <!--<blockquote>긴 인용문을 담을 때 사용!, 박스와 같은 성격</blockquote>-->

   <p>
    <!--형광펜 효과 -->
    <mark>중요한 부분을 강조할 때 사용>>형광펜으로  줄을 그은 것처럼 노란 배경색이 나타남!</mark>
   </p>

   <p>
    <!--span: 글자를 꾸밀 때 사용  스타일의 선택자와 함께 주로 사용-->
    글자를<span>꾸밀 때 사용</span>합니다.
   </p>

   <p>
    <!--동아시아 글자 표현, 주석: 동아시아 국가들 주석(발음)내용을 표기하기 위해 사용-->
    <ruby>
      韓國<rp>(</rp><rt>한국</rt><rp>)</rp>
    </ruby>
   </p>

   <p>
    <!--취소선,중간줄-->
    <del>문서에서 삭제된 텍스트나 지워야 할 부분 강조!</del>
   </p>

   <p>
    <!--밑줄-->
    <ins>문서에 나타난 텍스트에 강조하거나 밑줄 표현 시 사용</ins>
   </p>

   <p>
    <!--위첨자,아래첨자-->
    글자의 위로 붙는 <sup>위첨자</sup>
    글자의 아래로 붙는 <sub>아래첨자</sub>
   </p>

   <h1>Lorem Ipsum</h1>
   <p>
     <strong>Lorem Ipsum</strong> is simply dummy text of the printing and typesetting industry.<br/>
     Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, <br/>
     when an unknown printer took a galley of type and scrambled it to make a type specimen book. <br/>
     It has survived not only five centuries, <em>but also the leap</em> into electronic typesetting, remaining essentially unchanged. <br/>
     It was popularised in the 1960s with the release of <mark>Letraset sheets containing Lorem Ipsum passages</mark>, <br/>
     and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum<br/>
   </p>

   <br/>
   <br/>
   <br/>

   <h1>특수문자 표현!#@#</h1>
   <p>
    엔티티(entity): html에서 예약된 문자!16진수의 엔티티 숫자~<br/>

    <!--<  &lt; == &#60;   (보다 작은)
           &gt; == &#62;   (보다 큰)
          공백 >> &nbsp;  == &#160; (줄 바꿈 없는 공백) -->
    &#60; 특수문자 표현 &#62;
   </p>

</body>
</html>
```

## 강의 5. img, a 태그

### img 태그

이미지를 나타내는 단독 태그(`<img/>`). 글자와 같이 나열되는 성격이며, 이미지 단락 구분에는 `br`을 쓴다.

- 대표 확장자: `jpg`(색상 표현이 가장 좋음), `png`(색상 유지 + 투명 배경), `gif`(투명 배경 가능하나 256색, 움짤).
- 경로는 작성하는 문서를 기점으로 지정한다.
- `alt`: 이미지가 안 보일 때 대비한 대체 문자이며 HTML5 기본 규칙.
- `figure` / `figcaption`: 이미지, 사진, 삽화 콘텐츠와 캡션을 넣을 때 사용.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>img</title>
</head>
<body>
  <h1>img태그</h1>
  <p>
    : 이미지를 나타내줄 수 있는 태그/단독태그 <!--<img/>-->/글자와 같이 나열되는 성격,이미지의 단락을 구분 지을 때"br"
  </p>
  <!--
    이미지의 확장자(대표)
    jpg> 가장 대표적인 이미지 표현방식, 이미지의 색상을 가장 잘 표현할 수 있는 확장자!
    png> 이미지의 색상을 유지하며, 투명한 배경을 나타낼 수 있는 확장자
    gif>투명한 배경이 가능하나, 색상이 256개의 표현만 가능~ 화질이 떨어져 보임/ 움짤, 움직이는 이미지

    경로>> 폴더 안 >>/ *작성하는 문서의 기점으로부터
  -->
  <img src="indel.png"/><br/>
  <!--index 파일과 함께 존재하는 img폴더 안에(/)이미지를.확장자를 불러서 찾겠다!
    문서가 옆에 있을때는 바로 부르기
    alt: 주석문, 이미지가 안 보일때 대비한 대체문자이며 html5기본 규칙-->
  <img src="sdlfj.png" alt="몰라"/>

  <figure>
    <!--이미지나,사진,삽화같은 콘텐츠를 넣을 때 사용-->
    <img src="indel.png" alt="카메라03"/>
    <!--figure요소에 캡션을 넣을 때 사용하는 태그로 figure안에서 사용, 제일 처음이나 마지막에 배치-->
    <figcaption>카메라를 올바르게 촬영하는 방법</figcaption>
  </figure>

  <!--이미지태그를 url로 연결하는 방법-->
  <img src="https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_4x3.jpg " alt="url"/>

</body>
</html>
```

### a 태그

웹페이지 연결, URL 연결 시 사용(메뉴 표현). 글자와 같이 나열되며 기본 스타일(글자색, 밑줄, 손 모양 커서)이 있다.

- URL: `https://`(필수) 포함.
- 임시 링크: `#`.
- 메일 `mailto:`, 전화 `tel:`, 문자 `sms:`.
- `target="_blank"`: 새 창 전환(`_self`는 기본값, 현재 창).
- 내부 페이지 이동: 파일명 지정.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>하이퍼텍스트링크</title>
</head>
<body>
  <h1>a태그</h1>
  <p>
    :웹페이지의 연결, url연결 시 사용>>다른페이지의 전환(메뉴표현) /글자와 같이 나열되는 성격<br/>
    링크연결시 기본 스타일(글자색, 밑줄, 손모양의 커서 ),브라우저내에서 바로 전환
  </p>
  <!--여러가지 연결방법-->
  <!--01.인터넷주소.url>> https://(필수))-->
  <a href="https://www.naver.com">네이버</a><br/><br/>

  <!--02.임시링크,#-->
  <a href="#">임시링크</a><br/><br/>

  <!--03.메일(mailto),전화(tel),문자(sms) -->
  <a href="mailto:admin@example.com">관리자메일</a><br/><br/>

  <!--04.새창 전환
    target=링크된 문서를 클릭했을 때 문서가 열릴 위치를 지정
    _self= 기본값/현재의 브라우저에서 전환
    _blank= 새창전환/새로운 도메인창을 열 때
    -->
    <a href="https://www.naver.com" target="_blank">네이버</a><br/><br/>

  <!--05.메뉴를 눌러 서브페이지로의 전환>> 다른페이지로 이동-->
  <a href="index4-1.html">메뉴1</a>

</body>
</html>
```

## 강의 6. CSS 기초 - 선택자

- 전체 선택자 `*`: HTML 내 모든 요소를 선택(초기화, 기본 설정값).
- 태그 선택자: 특정 태그를 선택.
- 아이디 선택자: 본문 `id="name"` / 스타일 `#name`. 한 화면에서 하나의 이름을 한 번만 사용. 주로 큰 단락/부모에 사용.
- 클래스 선택자: 본문 `class="name"` / 스타일 `.name`. 여러 곳에서 여러 번 사용 가능. 주로 작은 요소, 변화가 잦은 스타일.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>css기초 -선택자</title>
  <style>
      *{
        padding:0;/*안쪽여백*/
        margin:0;/*바깥여백*/
        /*style안에 작성하는 주석방법.
        color:deeppink;*/
      }
      /*h1{
        color:coral; 글자색 부여: 단어,컬러코드(hex)
      }
      p{
        color:cornflowerblue;
      }*/
      #aa{
        color:blueviolet;
      }
      #bb{
        color:cadetblue;
        font-size:50px;
      }
      .cc{
        font-size:50px;
      }
  </style>
</head>
<body>
   <h1 class="cc">전체선택자</h1>
   <p>*{html내에 등장하는 모든 형태를 선택하는 선택자.(초기화,기본설정값)</p>

   <br/><br/><br/>

   <h1 id="bb">태그 선택자</h1>
   <p>h1,h2,p,a,img.../html내에 등장하는 특정한 태그를 선택하는 선택자.</p>

   <br/><br/><br/>

   <h1 id="aa">아이디선택자</h1>
   <p class="cc">
    :본문(id="name")/스타일(#) <br/>
    특정한 이름을 부여하여 선택하는 선택자로, html화면 내에서 하나의 이름으로 한번만 사용가능.
    주로 큰 단락,부모에서 사용, 위치이동, 이름
   </p>

   <br/><br/><br/>

   <h1 class="cc">클래스 선택자</h1>
   <P style="color:blue;">
    :본문(class="name")/스타일(.)<br/>
    특정한 이름을 부여하여 선택하는 선택자로,html화면 내에서 하나의 이름으로 여러군데 여러번 사용가능!<br/>
    주로 작은 요소, 작은 단락, 변화가 잦은 스타일
   </P>

</body>
</html>
```

## 강의 7. 글자/배경 관련 속성

- 글자: `color`, `font-size`, `font-weight`(100~900), `line-height`, `font-family`, `font-style`, `letter-spacing`, `text-align`.
- `a` 기본값 제거: `text-decoration:none`.
- 배경: `background-color`, `background-image:url(...)`, `background-repeat`(no-repeat / repeat-x / repeat-y / repeat), `background-size`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS속성</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    .text{
      color:crimson; /*글자색상-단어,hex*/
      font-size:20px;/*글자사이즈-px,em,pt...단위*/
      font-weight:900; /*글자의 굵기- 100~900(100~300가늘게),(400~600중간),(700~900굵게)
      서체마다 굵기가 적용되지 않을 수 있다.*/
      line-height:50px;/*행간,줄간격-px,em,pt,%...단위*/
      font-family:"궁서";/*글꼴 - 내 컴퓨터에 저장된 글자가 표현(웹폰트는 예외)*/
      font-style:italic; /*글자스타일-italic,normal*/
      letter-spacing:10px;/*자간,글자사이의 간격 - 숫자입력(px,%...)*/
      text-align:left; /*문단 정렬(글자 정렬) - left,right,center*/
    }
    a{
      text-decoration:none; /*<<(a태그에 대한 기본값)글자를 꾸며주는 속성*/
      color:crimson;
    }
    body{
      background-color:aquamarine;  /*배경색상*/
      /*background-image:url(img/bg.png); 배경이미지 속성>url(이미지의 경로)
      이미지의 사이즈가 부모의 사이즈보다 작을때 반복되는 성격
      공간,내용물이 있는 상태에서 나타남*/
      background-repeat:no-repeat; /*배경이미지의 반복 속성 > no-repeat(반복되지 않는 원본 한장)
      repeat-x(가로반복)  /  repeat-y(세로반복)     repeat(반복,기본값)*/
      background-size:100%; /*배경이미지 사이즈 속성 - x(가로폭),y(세로폭)px,%값*/
    }
    h1{
     /* background-color:brown;*/
    }
    p{
      background-image:url(img/bg.png);
    }
  </style>
</head>
<body>
  <!--
  <h1 class="text">글자관련 <a href="#">속성</a></h1>
  <p>
    글자관련 속성들에 대해 알아 봅시다.<br/>
    글자 속성들의 종류
  </p>
  -->
  <h1>배경관련 속성</h1>
  <p>
    배경색을 넣거나 배경이미지를 넣어서 공간을 활용<br/>
    배경색을 넣거나 배경이미지를 넣어서 공간을 활용<br/>
    배경색을 넣거나 배경이미지를 넣어서 공간을 활용<br/>
    배경색을 넣거나 배경이미지를 넣어서 공간을 활용<br/>
    배경색을 넣거나 배경이미지를 넣어서 공간을 활용<br/>
  </p>

</body>
</html>
```

## 강의 8. div, span (block / inline)

- `block`: 박스처럼 쌓이며 화면 전체 폭을 사용(div 등).
- `inline`: 글자처럼 옆으로 나열되며 내용만큼 폭을 차지(span 등). `width`, `height`, `margin-top`, `margin-bottom`이 적용되지 않음.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>박스의 성격</title>
  <style>
    div{
      background-color:coral;
      line-height:50px;/*행간,줄간격*/
    }
    span{
      background-color: aquamarine;
    }
  </style>
</head>
<body>
  <!--block: 박스와 같이 쌓이면서 나타나는 성격 / 화면 전체를 사용하는 태그-->
  <div>box1</div>
  <div>box2</div>
  <div>box3</div>

  <!--inline:글자와 같이 옆으로 나열되며 나타나는 성격/내용의 폭값,화면의 일부를 차지하는 태그
    / width,height,margin-top,margin-bottom= 적용되지 않음-->
  <span>span1</span>
  <span>span2</span>
  <span>span3</span>

</body>
</html>
```

box-size에 영향을 주는 스타일: `width`, `height`, `border`, `padding`, `margin`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>div</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    div{
      background-color: aquamarine;
      font-size:30px;
      font-weight:900;
      /*box-size에 영향을 주는 스타일*/
      width:300px;/*넓이,가로폭=px,%,auto*/
      height:300px;/*높이,세로폭=px,%,auto*/
      border:5px solid #000;/*선,선의굵기 선의스타일 선의색상*/
      padding:50px;/*안쪽여백,안쪽으로 내용물과 박스 사이의 틈 (한자리)전체면 적용*/
      margin:50px; /*바깥여백 - 바깥으로 박스혹은 다른 요소와의 틈, 간격(한자리 전체)*/
    }
    /* 실제박스사이즈
    width:50px;
    height:50px;
     */
  </style>
</head>
<body>
  <div>box1</div>

</body>
</html>
```

## 강의 9. width(%, auto) / padding / margin / border

- `width:100%`: 부모 기준 비율. 추가 요소를 포함하지 않고 넘칠 수 있음.
- `width:auto`: 추가 요소를 함께 가져가며 폭값을 유지하려 함.
- `padding`, `margin`: 한 자리(전체), 두 자리(상하/좌우), 네 자리(시계방향 위·오른쪽·아래·왼쪽). 개별 부여 가능(`padding-top` 등). `margin`에는 `auto`(중심 배치)도 가능.
- `border-width` / `border-color` / `border-style`(전체 적용), `border-radius`(모서리 둥글게).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    .box{
      width:100%;  /*%부모기준에 따른 양으로 표현 /추가되는 요소들을 포함하지 않고,넘치게 할 수 있음*/
      height:100px;
      background-color: bisque;
      padding: 10px;
    }
    .box2{
      width:auto;  /*%부모기준에 따른 양으로 표현 /추가되는 요소를 함께 가져가며 폭값을 유지하기 위해 노력*/
      height:100px;
      background-color:aquamarine;
      padding: 10px;
    }
    #id{
      width:500px;
      height: 250px;
      border: 5px solid #000;
    }
  </style>
</head>
<body>
  <div id="width">
    <div class="box">box</div>
    <div class="box2">box</div>
  </div>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>여백,사이즈</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    div{
      background-color: gray;
      width:300px;
      height:300px;
      color:white;
      font-size:30px;
      font-weight:900px;
      /* padding:30px 0px; 두자리 - 상하,좌우 네자리(시계방향 위쪽 오른쪽 아래쪽 왼쪽)
      개별부여가능*/
      padding-top:30px; /*bottom/right/left(margin옵션동일)*/
      margin:50px 100px; /*추가적으로 auto가능 중심배치*/
      /*border:3px solid black; 선-굵기 스타일 색상*/
      /*border-top:5px solid black;*/
      border-width:10px;/*선의 굵기-전체적용*/
      border-color:cadetblue;/*선의 색상-전체적용*/
      border-style: inset;/*선의 스타일-전체적용*/
      border-radius: 50px;/*모서리 둥글게 표현 px,%
                      1자리-4개의 모서리 전체 / 2자리 - 왼쪽 상단 시작 x / 4자리 시계방향(왼쪽 상단)*/
    }
  </style>
</head>
<body>
  <div>box</div>
</body>
</html>
```

## 강의 10. float, box-sizing

- `float`: 박스를 옆으로 나열할 때 사용(떠다니는 성격). 레이아웃 나열/삽화 삽입에 사용. `left` / `right`.
- `clear`: float 제거. `left` / `right` / `both`.
- `box-sizing:border-box`: 패딩과 선을 폭값 안에서 함께 계산.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div{
      width:500px;
      height:500px;
      border:5px solid black;
      padding:20px;
    }
    img{
      float:right;
      /*left:왼쪽으로부터 나열되게 / right:오른쪽으로부터 나열*/
    }
  </style>
</head>
<body>
  <!--float:박스를 옆으로 나열 할 때 사용/떠다니는 ~/레이아웃을 나열하거나 형성+삽화를 넣을 때-->
  <div>
    <img src="img/camera01.png" alt="">
    <h1>title</h1>
    <p>
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    Why do we use it?
    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
    The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here',
    making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text,
    and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident,
    sometimes on purpose (injected humour and the like).
    </p>
  </div>
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div{
      width:300px;
      height:300px;
      border:5px solid black;
      float:left;/*왼쪽으로부터 나열*/
      margin-right:30px;
    }
    .boxr{
      width:300px;
      height:300px;
      border:5px solid black;
      float:left;   /*옆의 박스에 영향을 주는 속성, 나열하고자 하는 박스함께 나열값*/
    }
    .boxc{
      width:500px;
      height:300px;
      margin:0;
      margin-top:30px;
      clear:both;
    }
    #allbox{
      float:none;
      border:none;
      margin:0 auto;
      background-color: aquamarine;
      width:720px; /*w=200*3(=600) + b:5*6(=30) + 30*3(=90)*/
      height:210px; /*h:200 + b:5*2(=10)*/
    }
    .boxs{
      padding:20px;
      box-sizing:border-box; /*패딩,선을 폭값안에서 함께 표현*/
    }
  </style>
</head>
<body>
  <!--float:박스를 옆으로 나열 할 때 사용/떠다니는 ~/레이아웃을 나열하거나 형성+삽화를 넣을 때-->
<div id="allbox">
  <div>1</div>
  <div>2</div>
  <div class="boxr">3</div>
</div>

  <!--clear:float와 함께 사용,float  제거 할 때 사용
      left:좌측 나열을 제거
      right:우측 나열을 제거
      both: 양쪽 나열을 제거
      <div class="boxc">제거할거야</div>-->

      <!--box-sizing:박스의 크기를 어떤 것의 기준으로 계산할지 지정하는 속성-->
      <div class="boxs">
        boxsizing
      </div>
</body>
</html>
```

## 강의 11. display

요소를 어떤 성격으로 보여줄지 결정하는 속성.

- `block`: 박스처럼 쌓이며 화면 전체 폭 사용(div, h, p, table, ul, ol...).
- `inline`: 글자처럼 나열되며 내용만큼 폭(a, span, i, em...).
- `inline-block`: 인라인과 블록의 합성. 옆으로 나열되면서 모든 CSS 적용.
- `none`: 안 보이게 처리.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>display</title>
  <style>
    *{
      padding: 0;
      margin:0;
    }
    div{
      background-color: aquamarine;
      width:300px;
      height:100px;
      margin:50px;
      /*모든 css 적용 - block*/
      /*display:inline;*/
    }
    span{
      background-color: blue;
      width:300px;
      height:100px;
      margin:50px;
      /*폭,width,height,margin - top, bottom 적용되지 않음*/
      display:block;
    }
  </style>
</head>
<body>
  <!--display:요소를 어떤 성격으로 보여줄지 결정하는 속성
    block:박스와 같이 쌓이는 성격 + 화면 전체의 폭을 사용하는 성격
    div / h/ p / table / ul / ol...

    inline: 글자와 같이 나열되는 성격 _ 내용물에 따라 폭이 결정되는 성격
    a.span.i.em...
  -->

  <div>block01</div>
  <div>block02</div>
  <div>block03</div>

  <span>inline01</span>
  <span>inline02</span>
  <span>inline03</span>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>display-응용</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    body{
      text-align:center;
    }
    span{
      border:4px solid black;
      /*인라인과 블록의 합성속성
      글자와 같이 옆으로 나열,블럭과 같이 css에 대한
      모든 적용이 이루어지는 성격
      inline-block*/
      display:inline-block;
      width:600px;
    }
    .transfrom{
      display:block;
      width:600px;
      margin:0 auto;
      display: none;/*안보이게 처리*/
    }
    div{
      background-color: aquamarine;
    }
  </style>
</head>
<body>
  <div>
  <span>span01</span>
  <span>span02</span>
  <span>span03</span>
</div>

  <span class="transfrom">span04</span>
  <span class="transfrom">span05</span>
  <span class="transfrom">span06</span>

</body>
</html>
```

## 강의 12. overflow, 목록 태그(ul, ol, dl)

- `overflow`: 부모 박스에서 내용물이 넘칠 때 표현 방법을 결정. `overflow-x` / `overflow-y`.
  - `hidden`: 영역을 벗어난 부분을 숨김(높이가 없을 때 높이를 대신하기도 함).
  - `scroll`: 넘칠 때 스크롤(넘치지 않아도 스크롤 생성).
- 목록: `ul`(순서 없는 목록, 메뉴/블릿), `ol`(순서 있는 목록), `dl`(정의 목록, `dt`/`dd`).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>overflow</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    body{
      /*1920*1080*/
      background-color: burlywood;
      width:2000px;
      height: 1500px;
      overflow-x:hidden ;/*x축(가로)의 넘치는 내용물을 어떻게 보여질지 결정하는 속성*/
      overflow-y:hidden;  /*y축(세로)의 넘치는 내용물을 어떻게 보여질지 결정하는 속성*/
    }
    .contents1{
      width:200px;
      height: 200px;
      border:2px solid black;
      float:left;
      margin:10px;
    }
    .contents2{
      width:200px;
      height: 200px;
      border:2px solid black;
      float:left;
      margin:10px;
    }
    .contents3{
      width:200px;
     /* height: 200px;*/
      border:2px solid black;
      float:left;
      margin:10px;
      overflow:hidden;
      /*영역을 벗어나는 부분을 보이지 않게 처리
        height존재하지 않을 때 높이를 대신*/
    }
    .contents4{
      width:200px;
      height: 200px;
      border:2px solid black;
      float:left;
      margin:10px;
      /*overflow:hidden; 폭값이 존재할 때
        내용물을 안보이게 처리*/
      overflow:scroll;
      /*안에 콘텐츠가 넘치는 경우 스크롤,
      내용물이 넘치지 않아도 자동 스크롤 생성*/
    }
  </style>
</head>
<body>
  <!--overflow: 부모박스에서 내용물이 넘치는 경우 어떻게 보여질지 결정하는 속성-->
  <div class="contents1">
    <h4>콘텐츠양이 일정</h4>
    <P>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
    </P>
  </div>
  <div class="contents2">
    <h4>콘텐츠양이 많거나 유동-흘러넘침</h4>
    <P>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
    </P>
  </div>
  <div class="contents3">
    <h4>콘텐츠양에 따라서 높이가 늘어나는 경우</h4>
    <P>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
    </P>
  </div>
  <div class="contents4">
    <h4>박스의 높이에 따라 콘텐츠가 안 보이게 처리 </h4>
    <P>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        It has survived not only five
    </P>
  </div>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>list</title>
  <style>
    li{
      /* list-style: square;li태그의 스타일을 결정하는 속성 -li 사용 시 기본설정값 none; */
      list-style-type: decimal-leading-zero; /*decimal -기본값*/
                                            /* decimal-leading-zero - 숫자값앞에 0이 붙는 속성*/
      list-style-type: lower-alpha;/*소문자*/
      list-style-type:upper-alpha;/*대문자*/
    }
  </style>
</head>
<body>
    <!--목록태그 ul( 순서가 없는 목록태그 - 메뉴/블릿)ul>li
    ol(순서가 있는 목록태그 - 순서나열/ 1,2,3~)ol>li
    dl(정의 목록태그, 용어 뜻을 나열)dl>dt.dd
    -----------------------------------------------
    안쪽에 속하는 태그들 함께 사용-->
  <!-- <ul>
    <li>회사소개</li>
    <li>생산설비</li>
    <li>제품소개</li >
    <li>온라인문의</li>
    <li>커뮤니티</li>
  </ul> -->

  <ol>
    <li>
      <li>회사소개</li>
      <li>생산설비</li>
      <li>제품소개</li>
      <li>온라인문의</li>
      <li>커뮤니티</li>
    </li>
  </ol>

  <dl>
    <dt>정의 목록 타이틀</dt>
    <dd>목록의 내용</dd>
  </dl>
</body>
</html>
```

## 강의 13. 선택자 - 후손/자손/동일/반응

- 기본/클래스/샵 선택자 복습.
- 후손 선택자 `A B`: A의 하위 요소 중 특정 요소를 모두 선택.
- 자손 선택자 `A > B`: A 바로 밑의 특정 요소를 선택.
- 동일(형제) 선택자: `A + B`(A 바로 뒤의 B), `A ~ B`(A 뒤의 B 모두).
- 반응 선택자: `:hover`(마우스를 올렸을 때), `:active`(클릭한 순간).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>다양한 선택자 01</title>
  <style>
    *{
      padding:0;
      margin:0;
    }
    div{
      background-color: beige;
    }
    .box{
      width:300px;
      height: 300px;;
    }
    #box{
      width: 200px;
      height:200px;
      margin:10px;
    }
  </style>
</head>
<body>
  <div class="box">선택자 복습</div>
  <div id="box">선택자 복습</div>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>선택자활용</title>
  <style>
    div>h1{/*자손css문법*/
      background-color: aquamarine;
    }
    div span {/*후손css문법*/
      background-color: burlywood;
    }
    div h2{
      border: 3px solid black;
    }
    div>span{
      color:crimson
    }
    .box span{
      font-size:40px;
    }
    h1+h2{
      color:crimson;
    }
    h1~h2{
      background-color: beige;
    }
    h1:hover{
      /*특정한 요소에 마우스를 올렸을 때*/
      background-color: blue;
    }
    h2:active{
      /*특정한 요소에 마우스로 클릭을 한 순간*/
      color:aqua;
    }
  </style>
</head>
<body>
  <!--후손 선택자 & 자손 선택자
  후손선택자 : 해당요소의 하위요소에 있는 특정한 요소를 모두 선택 / 선택자A 선택자B
  자손선택자 : 해당요소의 바로 밑에 위치하는 특정한 요소를 선택 /선택자A > 선택자B

  <div>
    <h1>제목1</h1>
    <h2>제목2</h2>
    <div class="box">
      <ul>
        <li>menu1</li>
        <li>menu2</li>
        <li><span>menu3</span></li>
      </ul>
    </div>
    <h2>제목2</h2>
    <span>span</span>
  </div>-->

  <!--동일 선택자
  :동일 관계에 있는 요소중에 해당요소보다 뒤에 존재하는 특정한 요소를 선택할 때 사용
  -선택자A + 선택자B : 선택자A 바로 뒤에 위치하는 선택자B를 선택
  -선택자A ~ 선택자B : 선택자A 뒤에 위치하는 선택자B를 모두 선택 -->

    <!--반응선택자 : 사용자가 마우스를 이용해서 혹은 특정한 행동(반응)을 취했을때 css속성을 지정할 수 있는 선택자-->
    <h1>제목1</h1>
    <h1>제목2</h1>
    <h1>제목2</h1>
    <h1>제목2</h1>
    <h1>제목2</h1>
    <h1>제목2</h1>

</body>
</html>
```

## 강의 14. 구조 선택자 (nth-child, of-type)

부모 요소 안에서 특정 위치의 요소를 선택. 후손/자손 선택자와 함께 많이 사용.

- `:first-child` / `:last-child`: 형제 관계에서 첫 번째 / 마지막 요소.
- `:nth-child(2n+1)`(홀수), `:nth-child(2n)`(짝수), `:nth-child(n)`(순번).
- 형태 구조 선택자: `:first-of-type`, `:last-of-type`, `:nth-of-type()` — 태그 형태를 구분해 선택.
- 추가: `:nth-last-child()`, `:nth-last-of-type()` — 뒤에서부터 순번.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>css의 활용2</title>
  <style>
    ul{
      overflow: hidden;
    }
    li{
      list-style:none;/*블릿 삭제*/
      float: left;
      padding: 15px;
    }

    /*li:first-child{같은 부모아래에서  형제관계에서 첫번째의 해당하는 요소를 선택
        background-color: beige;
    }*/

    li:last-child{
      /*부모 아래에서 형제관계의 마지막째에 해당하는 요소를 선택*/
      background-color: antiquewhite;
    }
    li:nth-child(2n+1){
      /*형제관계의 순번째의 위치하는 요소를 선택(1,2,3...)2n+1(홀수)2n(짝수)*/
      background-color: aqua;
      color:chocolate;
    }

    li:nth-child(2n){
      background-color: black;
      color:azure
    }
    li:nth-child(3){
    border:3px solid red;
    }
    li:nth-child(5) a{
      color:coral;
    }
    .box:first-child{
      background-color: darkgreen;
    }
    h1:first-of-type{
      background-color: beige;
    }
    h2:last-of-type{
      color:aqua;
    }
    h3:nth-of-type(2){
      border:2px solid black;
    }
      /*응용*/

    li:nth-child(5):hover{
    background-color: blueviolet;
    }
    li:nth-child(5):hover a{
      color:white;
    }

  </style>
</head>
<body>
  <!--구조선택자 : 부모의 요소 안에서 특정한 위치의 요소를 선택할 때 사용. 후손+자손선택자와 함께 많이 사용-->
  <ul>
    <li class="box">menu-1</li>
    <li class="box">menu-2</li>
    <li class="box">menu-3</li>
    <li class="box">menu-4</li>
    <li class="box"><a href="#">menu-5</a></li>
    <li class="box">menu-6</li>
  </ul>

  <!--형태구조선택자: 일반구조선택자와 비슷하지만 태그 형태를 구분
  :first-of-type == 부모박스 안에서 형제관계 중에 첫번째에 위치하는 태그를 선택
  :last-of-type == 부모박스 안에서 형제관계 중에 마지막번째에 위치하는 태그를 선택
  :nth-of-type == 부모박스 안에서 형제관계 중에 수열번째에 위치하는 태그를 선택
  :nth-last-of-type == 부모박스 안에서 형제관계 중에 뒤에서 수열번째에 위치하는 태그를 선택

  구조선택자 추가
  :nth-last-child() 부모박스 안에서 형제관계 중에 뒤에서 수열번째 위치하는 태그를 선택
  -->

  <div>
    <h1>header1</h1>
    <h2>header2</h2>
    <h3>header3</h3>
    <h3>header3</h3>
    <h2>header2</h2>
    <h1>header1</h1>
  </div>

</body>
</html>
```

## 강의 15. 속성/상태/가상요소 선택자

- 속성 선택자: `[속성="값"]`(일치), `[속성$="값"]`(끝남), `[속성*="값"]`(포함).
- 상태 선택자: `:focus`(초점), `:checked`(체크됨).
- 문자 선택자: `::first-letter`(첫 글자), `::first-line`(첫 라인).
- 가상요소 선택자: `::before`(앞에 삽입), `::after`(뒤에 삽입) — `content`로 내용 부여.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>선택자의 활용</title>
  <style>
    input[type="text"]{
      background-color: coral;
    }
    img[src$="png"]{
      border: 3px solid #f00;
    }
    img[src$="jpg"]{
      border: 3px solid #f00;
    }
    img[src$="gif"]{
      border: 3px solid #f00;
    }
    div[class*="box"]{
      background-color: aqua;
    }
    input:focus{
      /*input에 초점이 맞춰진 상태*/
      background-color: aqua;
    }
    div{
      width: 650px;
      height: 300px;
      background-color: antiquewhite;
      overflow:hidden;
    }
    /*:checked input에 check가 된 상태*/
    input[type="checkbox"]:checked+div{
      background-color: aqua;
    }
    /*+동일선택자 바로 뒤에 위치하는 특정요소를 선택*/

    /*문자선택자: */
    p::first-letter{
      /*특정한 선택자의 첫번째 글자를 선택*/
      font-size: 20px;
      font-weight: 900;
      color:aqua
    }
    p::first-line{
      /*특정한 선택자의 첫번째 라인*/
      background-color: cornflowerblue;
    }
    h1::before{
      content:'앞쪽>';
      font-size: 30px;
      font-weight: 900;
      color:aquamarine;
    }
    p::after{
      content:'<뒤쪽';
      font-size: 30px;
      font-weight: 900;
      color:aquamarine;
    }

  </style>
</head>
<body>
  <!--속성선택자: 특정한 속성값을 가지고 있는 html의 요소를 선택
  [속성이름="속성값"]
  [속성이름$="속성값"]
  [속성이름*="속성값"]

  <input type="text"/>

  <div class="box">
    <img src="img/camera01.png" alt="">
    <img src="img/camera02.jpg" alt="">
    <img src="img/camera03.gif" alt="">
  </div>-->

  <!--상태선택자: 마우스의 반응에 따른 상태를 선택-

  <input type="text"/>-->

  <br/>
  <input type="checkbox"/>

  <!--
    가상요소선택자
    선택될 요소의 앞 혹은 뒤쪽으로 가상의 요소를 넣어 표현.
    ::before 특정요소의 앞에 삽입,내용이나 가상의 요소를 부여
    ::after 특정요소의 뒤에 삽입, 내용이나 가상의 요소를 부여
  -->
  <div>
    <h1>Lorem Ipsum</h1>
    <p>
      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
      Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
      when an unknown printer took a galley of type and scrambled it to make a type specimen book.
       It has survived not only five centuries, but also the leap into electronic typesetting,
       remaining essentially unchanged. It was popularised in the 1960s with the release
       of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop
       publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    </p>
  </div>

</body>
</html>
```

> 참고: 원본 코드에는 `p::first-lint`, `h1::befor`, `input[type=":checkbox"]` 등의 오타가 있었으나, 학습 취지에 맞게 올바른 표준 표기(`::first-line`, `::before`, `[type="checkbox"]`)로 교정했다.

## 강의 16. background 속성

- `background-image:url(...)`: `,`로 구분해 2장 이상 적용 가능(먼저 작성한 이미지가 상단).
- `background-repeat`: `no-repeat` / `repeat-x` / `repeat-y`.
- `background-size`: `%`, `px`, 또는 `cover`(가로세로 비율 유지하며 꽉 채움).
- `background-attachment`: `fixed`(스크롤해도 고정) / `scroll`(기본값).
- `background-position`: `x y`(단어/px/%). x: left, center, right / y: top, center, bottom.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    *{
      padding: 0;
      margin:0;
    }
    body{
    /*background-image: url(img/cat_bg.png),url(img/land.png);
    배경이미지를 불러오는 속성,url(이미지의 경로,url)-반복되는 성격
   ,로 구분지어 배경이미지를 2장 이상 적용 먼저 작성한 이미지가 상단에서 표현~*/
      /* background-image: url(img/art.jpg); */
      background-repeat:no-repeat;
      /*배경이미지의 반복- no-repeat(반복하지 않은 원본 한장)
       repeat-x(가로반복)
       repeat-y(세로반복)*/
       background-size: 500px 300px;
       /*배경이미지 사이즈%(가로상의 비율)
        x y>>%,px
        cover:화면상 꽉차게 표현, 가로세로의 비율을 유지
       */
       /*height:3000px;
       background-attachment:fixed; 스크롤바가 움직여도 배경이미지가 고정*/
       /*scroll기본값*/
       /*배경이미지를 어떤 방식으로 화면에서 표현할지 지정하는 속성*/
       background-position:left top ;
       /*배경이미지의 위치를 지정하여 표현가능한 속성
        x y >> 단어,px,%
        x(left,center,right)
        y(top,center,bottom)*/
    }
    div{
      background-color: aquamarine;
      /* width:500px;
      height:500px; */
      background-image: url(img/cat_bg.png);
      background-size: 100%;
    }

  </style>
</head>
<body>

  <div>
    공간주기
  </div>

</body>
</html>
```

> 공간(내용물)이 있어야 배경 이미지가 나타난다.

## 강의 17. color (hex, rgb, rgba, hsl, hsla)

- `단어`: 색상 이름으로 입력.
- `#f00`(hex): 반복되는 2자리는 한 자리로 축약 가능.
- `rgb(255,0,0)`: 0~255.
- `rgba(255,0,0,0.5)`: alpha(투명도) 0~1.
- `hsl(0,100%,50%)`: hue, saturation, lightness.
- `hsla(...)`: hsl + alpha.
- `opacity`: 요소 전체 투명도(자식 요소 포함, 상속됨).
- `box-shadow` / `text-shadow`: x축 y축 흐림크기 색상.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>다양한 색상</title>
  <style>
    *{padding:0; margin:0;}
    div{
      width:100%;
      height:100px;
      font-size:20px;
      text-align: center;
      line-height: 100px;/*글자의 높이가 부모박스의 높이와 동일하면 상하선상 중심배치, 글자가 한 줄일때만*/
    }
    /*공통된 빨간색 부여*/
    #word{background-color: red;}
    #hex{background-color: #f00;/*반복되는 2자리는 한자리로 줄여서 표현*/}
    #rgb{background-color: rgb(255,0,0);
    /*256개 / 0~255개*/
    }
    #rgba{
      background-color: rgba(255,0,0,0.5);
       /*색상에 대한 투명도 0~1사이의 소수점*/
    }
    #hsl{
      background-color: hsl(0,100%,50%);
      opacity: 0.5;
      /*요소의 투명도를 부여하는 속성,0~1사이의 소수점=값
      상속=자식요소를 포함한 모든 부분의 투명도가 적용*/
    }
    #hsla{
      background-color: hsla(0,100%,50%,0.5);
    }
    p{
      width:300px;
      height: 300px;
      background-color: #c8d3ff;
      text-align: center;
      line-height: 300px;
      margin: 100px;
      box-shadow:5px 5px 10px black;
      /*박스 그림자 속성: x축 y축 그림자크기 그림자색상*/
      font-size:30px;
      font-weight: 900px;
      color:white;
      text-shadow: 5px 3px 7px gray;
      /*글자의 그림자 속성: x축 y축 그림자크기 그림자색상*/
    }

  </style>
</head>
<body>
  <div id="word">단어: 단어로 입력하는 방식</div>
  <div id="hex">컬러코드: #웹번호로 입력하는 방식</div>
  <div id="rgb">rgb : red,green,blue 의 숫자값을 입력하는 방식 </div>
  <div id="rgba">rgba: rgb표현방식에 alpha값이 추가</div>
  <div id="hsl">hsl : hue,saturation,lightness의 양값을 입력하는 방식</div>
  <div id="hsla">hsla : hsl표현방식에 alpha값이 추가</div>

  <p>
    box
  </p>

  <!-- ColorZilla 그라데이션 -->
</body>
</html>
```

## 강의 18. 시맨틱 구조 & 외부 CSS

- 시맨틱 태그: `header`, `nav`, `section`, `article`, `aside`, `footer`.
- 외부 스타일 연결: `<link href="파일.css" rel="stylesheet" type="text/css">`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>시맨틱구조 제작</title>
  <link href="semantic-1style.css" rel="stylesheet" type="text/css">
  <!--외부스타일연결구문-->
</head>
<body>
  <!-- header -->
  <header>
    <h1>logo</h1>
    <nav>
      <ul>
        <li>menu-1</li>
        <li>menu-2</li>
        <li>menu-3</li>
      </ul>
    </nav>
  </header>
  <!-- //header -->

  <!-- section -->
  <div id="wrap">
    <!-- left -->
    <section>
      <article>
        <h2>Main Article</h2>
        <p>colorZilla for Google Chrome is an extension that assists web developers and
          graphic designers with color related tasks - both basic and advanced. ColorZilla
          includes a Color Picker, Eye Dropper, Gradient Generator and many additional advanced
           color tools.
          </p>
      </article>
      <article>
        <h2>Main Article</h2>
        <p>colorZilla for Google Chrome is an extension that assists web developers and
          graphic designers with color related tasks - both basic and advanced. ColorZilla
          includes a Color Picker, Eye Dropper, Gradient Generator and many additional advanced
           color tools.
          </p>
      </article>
      <article>
        <h2>Main Article</h2>
        <p>colorZilla for Google Chrome is an extension that assists web developers and
          graphic designers with color related tasks - both basic and advanced. ColorZilla
          includes a Color Picker, Eye Dropper, Gradient Generator and many additional advanced
           color tools.
          </p>
      </article>
    </section>
    <!-- //left -->
    <!-- right -->
    <aside>
      <h2>Right aside</h2>
      <p>
        ColorZilla for Google Chrome is an extension that assists web developers and
         graphic designers with color related tasks - both basic and advanced.
      </p>
    </aside>
    <!-- //right -->
  </div>
  <!-- //section -->

  <!-- footer -->
  <footer>
    <p>HTML5 COPYRIGHT</p>
  </footer>
  <!-- //footer -->

</body>
</html>
```

## 강의 19. 멀티미디어 요소 (audio, video, iframe)

- `audio`: 사운드 재생. `src`, `controls`, `muted`, `loop`. `source`로 여러 포맷 제공 가능.
- `video`: 영상 재생. `src`, `controls`, `muted`, `width`, `height`, `poster`(시작 이미지), `preload`.
- `iframe`: 내부 프레임(HTML 문서 안의 HTML 문서). 유튜브 등 큰 용량 영상을 링크로 가져올 때 사용.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>멀티미디어</title>

</head>
<body>
  <h1>멀티미디어</h1>
  <!-- html5에서 음악이나 오디오같은 사운드를 재생하기 위해 사용, 태그하나만으로 멀티미디어 기기에서 재생이 가능
        src="오디오 파일의 위치를 연결"
        controls="화면에서 재생 컨트롤 막대표시"
        muted="오디오가 재생중이지만 소리를 끔(음소거)"
        loop="반복재생"
  <audio src="/무제 폴더/file/test_ado.mp3" controls muted loop></audio>
  <audio>
    <source src="/무제 폴더/file/test_ado.mp3" type="audio/mp3">
    <source src="/무제 폴더/file/test_ado.ogg" type="audio/ogg">
    <p>오디오 파일이 브라우저에서 지원되지 않습니다.</p>
  </audio>-->

  <!-- video:html5에서 영상을 실행시키기 위해 사용. 비디오와 같은 영상 스트리밍을 재생할때 사용
        src="비디오 파일을 연결할때 사용"
        controls="비디오 재생 컨트롤 막대표시"
        muted="음소거/비디오는 재생"
        width="가로폭"
        height="높이"
        poster="비디오 재생 시작전 준비화면, 시작이미지(url연결) - 연결하지 않을 시 영상의 시작화면" -->
        <video src="/무제 폴더/file/korea_video.mp4" controls muted poster="/무제 폴더/file/bg.PNG" width="400" height="200" preload="none"></video>

        <!-- iframe: 내부프레임/html문서안에 html문서가 존재
                      긴내용의 문서, 유튜브영상 등 큰용량의 영상을 간단하게 링크로 가져올 때 많이 사용
                    src="가져올 링크 지정"
                  width="가로"
                height="세로"-->
                <!-- <iframe src="멀티미디어 copy.html" width="400" height="400" frameborder="0"></iframe> -->
                <iframe width="692" height="389" src="https://www.youtube.com/embed/dy6EFEPMOi4" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</body>
</html>
```

## 강의 20. table 태그

- 구조: `table` > `tr`(행) > `td`(열). `th`는 머리 칸(가운데 정렬 + 볼드).
- `caption`: 표 제목.
- 병합: `colspan`(가로 병합), `rowspan`(세로 병합).
- 의미 구조: `thead`, `tbody`, `tfoot`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>table</title>
  <style>
    td,table,th{border: 2px solid black;}
    td,th{width: 100px;}
  </style>
</head>
<body>
  <h1>표관련 태그</h1>
  <!-- 표를 나타내는 태그
    table > tr(줄,행) > td(칸,열) -->
    <table>
      <caption>table의 제목(center)</caption>
      <tr>
        <!-- th:table의 head 구분을 지을때 사용
            text-align:center / font-weight:bold -->
        <th>table1</th>
        <th>table2</th>
      </tr>
      <tr>
        <td>table3</td>
        <td>table4</td>
      </tr>
      <tr>
        <td>table5</td>
        <td>table6</td>
      </tr>
    </table>

    <br/><br/><br/><br/><br/>

    <table>
      <caption>table의 병합</caption>
      <tr>
        <td colspan="3">01</td>
        <!-- <td>02</td>
        <td>03</td> -->
        <td rowspan="3">04</td>
      </tr>
      <tr>
        <td rowspan="2">05</td>
        <td>06</td>
        <td>07</td>
        <!-- <td>08</td> -->
      </tr>
      <tr>
        <!-- <td>09</td> -->
        <td>10</td>
        <td>11</td>
        <!-- <td>12</td> -->
      </tr>
    </table>

    <br/><br/><br/><br/><br/>

    <table>
      <caption>표의 구조(의미)</caption>
      <thead>
        <tr>
          <th>table머리</th>
          <th>table머리</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>table내용</td>
          <td>table내용</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td>table하단</td>
          <td>table하단</td>
        </tr>
      </tfoot>
    </table>

</body>
</html>
```

## 강의 21. table 스타일

- `border-collapse`: `separate`(기본값, 틈 있음) / `collapse`(선 병합).
- `border-spacing`: 테두리와 셀 간격(2자리 - 수평 수직).
- `empty-cells`: `show` / `hide`.
- `vertical-align`: 수직 정렬(td 기본값 `middle`), `top` / `bottom`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>table_style</title>
  <style>
    *{padding:0; margin:0}
    table{
      border: 2px solid black;
      margin:100px;
      /*border-collapse: collapse;
      table과 td 사이 선값의 결합 유무를 결정하는 속성
        separate(기본값 - 틈이생긴상태)
        collapse(선과 선사이의 틈을 병합)-table표현시 기본값 */
        /*border-spacing:20px 40px
        테두리와 셀들의 간격을 지정하는 값
          2자리 입력 - 수평 수직 */
          /* empty-cells: show;
           빈셀의 보여지는 유무를 결정-hide(사라지게) show(나타나게) */
           border-collapse: collapse;
    }
    td{
      border: 2px solid black;
      width: 100px;
      height: 40px;
      text-align: center;
      vertical-align: middle;
      /* 수직에 대한 정렬 - td칸은 middle기본값
        top-위쪽 / bottom-아래쪽 */
    }
  </style>
</head>
<body>

  <table>
    <tr>
      <td>01</td>
      <td>02</td>
      <td>03</td>
    </tr>
    <tr>
      <td>04</td>
      <td>05</td>
      <td>06</td>
    </tr>
  </table>

</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    *{padding:0; margin: 0;}
    table{
      border-collapse: collapse;
      border-top:2px solid black;
      margin:40px auto;
      width: 300px;
    }
    td.th{
      width: 100px;
      height: 50px;
      text-align: center;
      border:1px solid aliceblue;
    }
    th{
      background-color: gray;
    }
    .bl_n{
      border-left: none;
    }
    .br_n{
      border-right: none;
    }
  </style>
</head>
<body>

  <table>
    <tr>
      <th class="bl_n">tit1</th>
      <th>tit2</th>
      <th class="br_n">tit3</th>
    </tr>
    <tr>
      <td class="bl_n">01</td>
      <td>02</td>
      <td class="br_n">03</td>
    </tr>
    <tr>
      <td class="bl_n">04</td>
      <td>05</td>
      <td class="br_n">06</td>
    </tr>
  </table>

</body>
</html>
```

## 강의 22. form / input

웹페이지에서 입력 양식의 그룹. 정보를 서버로 전달받기 위한 폼.

- 폼 속성: `name`(폼 이름), `method`(전송 방식 - `get`은 주소창에 노출, `post`는 내부 전송).
- `fieldset`(그룹화), `legend`(정의), `label`(용도/내용), `input`(서식).
- input type: `text`, `password`, `tel`, `checkbox`(다중), `radio`(단일), `submit`, `reset`.
- 그 외: `button`, `select`/`option`, `textarea`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>form</title>
  <style>
    input[type="text"]{
      background-color: beige;
      border:3px solid black;
    }
  </style>
</head>
<body>
  <!-- 웹페이지에서의 입력양식의 그룹/ 원하는 정보를 연결하여 전달받기 위한 명확한 폼양식
      [폼에 쓰이는 속성]
      name="폼의 이름/식별하기 위한 이름을 지정"
      method="폼을 서버로 전송할때 http메소드를 지정(=전송방식)"
      get="주소표시줄에 사용자가 입력한 내용이 그대로 표시"
      post="대부분이 사용하는 방식,내부적으로 보이지 않게 전송"-->
  <form >
    <!-- fieldset:특정한 엘리먼트끼리 그룹화
          legend:fieldset안에서 정의를 부여
          label: 해당 서식의 용도,내용
          input="서식" type="속성" name="이름" -->
    <fieldset>
      <legend>개인정보작성</legend>
      <label>id</label>
      <input type="text" name="id"/>
    </fieldset>

    <br>
    <!-- 비밀번호 입력양식 - 암호화된 입력 -->
    <input type="password" name="pw">

    <br><br>

    <!-- 전화번호 입력양식 - 모바일 확인 시 숫자키패드 -->
    <input type="tel" placeholder="010-0000-0000" name="tel">

    <br><br>

    <!-- 체크박스 - 다중선택 혹은 선택시 사용 -->
    <input type="checkbox" name="ch">
    <!--  라디오버튼 - 단일항목 선택 사용-->
    <input type="radio" name="r">

    <br><br>
    <!-- 버튼-submit(제출,확인) / reset(회수, 다시) -->
    <input type="submit" value="확인하기" name="btn">
    <input type="reset" value="취소하기" name="btn">

    <!-- 버튼태그,type="button" 일반버튼형태 -->
    <button type="button">버튼</button>

    <!-- 셀렉트 박스: 펼쳐진 상태에서 항목을 고르는 서식 -->
    <select>
      <option>항목1</option>
      <option>항목2</option>
      <option>항목3</option>
      <option>항목4</option>
      <option>항목5</option>
    </select>

    <br><br>
    <!-- 많은 내용의 글을 넣을때 사용하는 태그 -->
    <textarea></textarea>

  </form>

</body>
</html>
```

## 강의 23. 웹폰트

- 웹폰트: 링크/도메인/브라우저와 상관없이 웹페이지 내에서 폰트가 연결되는 것.
- 방법 1) 내 컴퓨터에 설치된 폰트를 스타일로 지정.
- 방법 2) CDN(링크)으로 서버상의 폰트를 가져오기 — 느려지거나 폰트가 안 나올 수 있음.
- 방법 3) `@font-face`로 폰트 파일을 문서와 직접 연결해 선언 — 빠르고 오류가 적음.
- 확장자: EOT(IE8 이하), TTF(기본), WOFF(대부분 브라우저 지원 좋음), WOFF2(압축률 더 좋음).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap" rel="stylesheet">
  <style>
     @font-face{
      font-family: 'nanum'; /*폰트이름 선언*/
      font-weight: 500; /*폰트의 굵기 지정*/
      src:url(/HTML5-CSS3/JMJ_23/설치/NanumFontSetup_TTF_ALL/NanumBarunGothic.ttf),
      url(/HTML5-CSS3/JMJ_23/설치/NanumFontSetup_TTF_ALL/NanumBarunGothicBold.ttf) format("woff");
    }
    *{padding:0; margin: 0;}
    /* body{
      font-size: 14px;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .test1{
      font-family: 'Courier New', Courier, monospace;
    } */
    P{margin:40px 0px;}
    .test2{font-family: 'Black Han Sans', sans-serif;}

   .test3{
    font-family:"nanum";
   }

  </style>
</head>
<body>
  <h1>웹폰트</h1>
  <p class="test1">
    webfont - 어떠한 링크,도메인,브라우저와 상관없이 웹페이지내에서 폰트가 연결되어지는 것<br>
    일반적으로 스타일을 이용해서 연결하는방법 - 내컴퓨터 내에 설치된 폰트가 존재
  </p>

  <p class="test2">
    webfont- cdn 즉 링크를  이용해서 서버상의 폰트를 가져와서 웹페이지에 전달하는 방법 -느려지거나,폰트가 나타나지 않는 경우가 생길 수 있음
  </p>
  <p class="test3">
    @font-face
    :폰트파일을 다운받거나, 가져와 문서와 직접 연결을 하여 폰트를 선언하는 방식 - 빠르게 웹사이트에 적용, 오류가 적음
    <br>
    웹폰트 확장자 종류
    -EOT:IE8이하
    -TTF:가장 기본, 압축을 푸는 형태로 많이 사용
    -WOFF:대부분의 브라우저에서 지원이 좋음
    -WOFF2:WOFF보다 압축률이 더 좋음
  </p>

</body>
</html>
```

## 강의 24. 웹 페이지 만들기 (레이아웃 실습)

지금까지 배운 태그와 float 레이아웃으로 header / section / footer 구조의 웹페이지를 구성한다.

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Alfredo gonzales</title>
  <link rel="stylesheet" href="finalcss.css" type="text/css">
</head>
<body>

  <!-- header -->
  <header>
    <a href="#" class="logo">Alfredo<br/>gonzales</a>
    <ul>
      <li><a href="#"><img src="/무제폴더/layout/images/menu01.png"  alt="이미지">home</a></li>
      <li><a href="#"><img src="/무제폴더/layout/images/menu02.png" alt="이미지">shop</a></li>
      <li><a href="#"><img src="/무제폴더/layout/images/menu03.png" alt="이미지">custombox</a></li>
      <li><a href="#"><img src="/무제폴더/layout/images/menu04.png" alt="이미지">blog</a></li>
      <li><a href="#"><img src="/무제폴더/layout/images/menu05.png" alt="이미지">story</a></li>
    </ul>
  </header>
  <!-- /header -->

  <!-- mainBg -->
  <section id="mainBg">
    <div class="left">
      <img src="/무제폴더/layout/images/header01.jpg" alt="">
    </div>
    <div class="right">
      <img src="/무제폴더/layout/images/side01.jpg" alt="">
      <div class="tbox">
        <p>DESIGN YOUR OWNSOCK</p>
        <h1>THE WORKSHOP</h1>
        <div class="line"></div>
      </div>
      <div class="tbox">
        <p>SELF SERVICE</p>
        <h1>ONLINE STORE</h1>
        <div class="line"></div>
      </div>
    </div>
  </section>
  <!-- /mainBg -->

  <!-- section01 -->
  <section id="section01">
    <div class="left">
      <img src="/무제폴더/layout/images/banner_01.jpg" alt="">
      <div class="ibox">
        <iframe src="https://player.vimeo.com/video/104136276" width="784" height="480" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
      </div>
    </div>
    <div class="right">
      <img src="/무제폴더/layout/images/banner_02.jpg" alt="">
    </div>

  </section>
  <!-- /section01 -->

  <!-- section02 -->
    <section id="section02">
      <img src="/무제폴더/layout/images/banner_03.jpg" alt="">
      <img src="/무제폴더/layout/images/banner_04.jpg" alt="">
      <img src="/무제폴더/layout/images/banner_05.jpg" alt="">
    </section>
  <!-- /section02 -->

  <!-- footer -->
    <footer>
      <div class="left"><!--배경이미지가 나타날 자리-->
        <!-- <img src="/무제폴더/layout/images/banner_bg.jpg" alt=""> -->
      </div>
      <div class="right">
        <div class="ibox">
          <iframe src="https://player.vimeo.com/video/58451361" width="800" height="340" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
        </div>
        <form>
          <div class="center">
            <label>SIGN UP</label>
            <input type="email" placeholder="YOUR EMAIL ADDRESS" name="em">
            <button type="button">&#62;</button>
          </div>
        </form>
      </div>
      <div class="footerlogo">
        Alfredo<br>gonzales
      </div>
    </footer>
  <!-- /footer -->

</body>
</html>
```

### CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Caveat:wght@600;700&family=Raleway:wght@100;200;300;400;500;600;700;800&display=swap');

*{padding:0; margin:0; font-family: 'Raleway', sans-serif;}
ul,ol{list-style: none;}
img{display:block;}
a{text-decoration: none; color:#333;}

header{
  width:1600px;
  overflow:hidden;
  margin:auto;
  text-align: center; /*글자의 성격 중앙정렬*/
  padding:40px 0px;
}
.logo{
  font-family: 'Caveat', cursive;
  font-size: 35px;
  line-height: 26px; /*다시 보기*/
  font-weight: 900;
  display: block;
}
header ul{
  display: inline-block;
  overflow: hidden;
}
header li{
  float:left;
  margin:20px;
  text-align: center;
}
header li img{
  margin:0 auto; /*다시 보기 block inline*/
}
header li a{
  font-weight: 600;
  display: block;
  padding-bottom: 5px;
}
header li:hover a{
  border-bottom: 2px solid #f00;
}
section{
  width:1600px;
  overflow:hidden;
  margin:0px auto;
}
#mainBg>.left{
  width: 1274px;
  float:left;
}
#mainBg>.right{
  width:316px;
  overflow: hidden;
  float: right;
}
#mainBg .tbox{
  width: 316px;
  height: 160px;
  border: 5px solid black;
  text-align: center;
  padding:15px 0px;
  box-sizing: border-box;
  margin-top:10px;
  background-image: url(../무제폴더/layout/images/box_bg.png);
}
#mainBg .tbox>p{/*선택자*/
  font-size:18px;
}
#mainBg .tbox>h1{
  margin:15px 0px;
}
#mainBg .tbox>.line{
  width:40px;
  height: 2px;
  background-color: #000;
  margin:0 auto;
}
#section01{
  margin-top: 30px;
}
#section01>.left{
  width: 784px;
  overflow:hidden;
  float:left
}
#section01>.right{
  width:785px;
  float:right;
}
#section01 .ibox{
  width:784px;
  height: 481px;
  background-color: #000;
  margin-top:30px;
}
#section02 img{
  margin-top:30px; /*auto*/
}
footer{
  width: 1600px;
  overflow: hidden;
  margin:0 auto;
  margin-top: 30px;
}
footer>.left{
  width: 790px;
  height: 500px;
  float: left;
  background-image: url(../무제폴더/layout/images/banner_bg.jpg);
  background-size: 790px 500px;
}
footer>.right{
  width: 800px;
  float: right;
  overflow: hidden;
}
footer .ibox{
  width: 800px;
  height:340px;
  background-color: black;
  overflow: hidden;
  margin-bottom: 10px;
}
footer form{
  width: 800px;
  height: 150px;
  background-color: #e68238;
  text-align: center;/*글자를 이용해서 중앙정렬*/
  overflow: hidden;
}
footer .center{
  display: inline-block;
  height: 40px;
  margin: 55px 0px;
}
footer label{
  font-size: 18px;
  line-height: 40px;
  font-weight: 800px;
  display: block;
  float: left;
  margin-right: 15px;
}
footer input[type="email"]{
  width:250px;
  height: 40px;
  display:block;
  float:left;
  padding-left:20px;
  font-size: 18px;
  border: none;
}
footer button{
  display: block;
  float:left;
  border:none;
  padding:0px 10px;
  height: 40px;
  font-size:14px;
  color:white;
  background-color: #000;
}

.footerlogo{
  text-align: center;
  font-weight: 900px;
  font-size:30px;
  clear:both;
  padding:30px 0px;
}
```

## 강의 25. position

요소를 특정 위치로 지정하여 배치하는 속성. 위치값 `left`, `right`, `top`, `bottom`과 함께 사용.

- `static`: 기본값(위치 영향 없음).
- `relative`: 상대 위치(박스가 나열되는 순서를 기준).
- `absolute`: 절대 위치(HTML 화면 기준. 부모가 있으면 부모 기준).
- `fixed`: 고정 위치(화면 기준, 스크롤해도 고정) — 메뉴, 배너에 사용.
- `z-index`: 위치 요소의 우선순위(1~9999).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>position</title>
  <style>
    *{padding:0; margin:0;}
    .p1{
      width: 300px;
      height: 300px;
      background-color: aquamarine;
      text-align: center;
      line-height: 300px;
      font-size: 30px;
      position: fixed;
      /* 위치지정시 사용가능한 속성 - left,right,top,bottom
      static - 기본값(위치 영향을 받지 않음)
      relative - 상대위치(박스가 나열되는 순서대로 위치가 지정 top,left)
      absolute - 절대위치(html화면 기준으로 위치가 지정 - 위칫값 모두적용)
      부모가 존재할때 부모의 기준으로 위치가 지정
      fixed - 고정위치(html 화면 기준으로 위치가 지정 - 위치모두적용)
      고정된 상태로 표현! - 메뉴,배너)
      */
      bottom:50px;
      right:50px;
    }
    body{
      height: 3000px;
      background-color: aliceblue;
    }

    .pbox{
      width: 200px;
      height: 200px;
      background-color: aquamarine;
      text-align: center;
      line-height: 200px;
      position: absolute;
      top:30px;
      left:30px;
    }
    .pbox:nth-child(1){
      z-index: 3;  /*위치요소의 우선순위를 변경하는 속성 1-9999*/
    }
    .pbox:nth-child(2){background-color: beige;      position: absolute;
      top:60px;
      left:60px;
      z-index: 4;
 }
    .pbox:nth-child(3){background-color: burlywood;      position: absolute;
      top:90px;
      left:90px;
}
    #position{
      width: 400px;
      height: 200px;
      background-color: beige;
      /* margin:100px; */
      position:relative;    /*부모기준을 삼으며, 다른 박스의 영향을 받아 레이아웃이 제대로 표현되어 질 수 있게*/
    }
    .nav{
      width:100%;
      height: 200px;
      text-align: center;
      background-color: aquamarine;
    }
      </style>
</head>
<body>
  <!-- <h1>position</h1>
  <p>:요소를 특정한 위치로 지정하여 배치하는 속성/ 어떻게 위치할지 결정하는 요소</p>

  <div class="p1">
    position
  </div> -->
    <div class="nav">
      menu
    </div>

  <!-- 위치값을 사용하는 방법 -->
  <div id="position">
    <div class="pbox">box1</div>
    <div class="pbox">box2</div>
    <div class="pbox">box3</div>
  </div>

</body>
</html>
```

## 강의 26. position 응용 & 레이아웃

`position:absolute` + `top:50%; left:50%` 후 `margin`으로 절반만큼 되돌려 중앙 배치하는 기법, 고정 헤더(`fixed`), 슬라이드 좌우 버튼 배치 등.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>position</title>
  <style>
    *{padding:0; margin:0;}

    #mainSlide{
      width:100%;
      height: 700px;
      overflow:hidden;
      background-image: url(/무제폴더/img/bg.jpg);
      background-size: cover;
      position:relative;/*부모 기준*/
    }

    #mainSlide>button{
      width: 100px;
      height: 100px;
      background-color: rgba(255,255,255,0);
      font-size:30px;
      color:#fff;
      border:1px solid #fff;
    }
    #mainSlide>button:nth-of-type(1){
      position: absolute;
      left:30px;
      top: 50%;
      margin-top:-50px;/*높이의 반만큼 되돌아가기*/
    }
    #mainSlide>button:nth-of-type(2){
      position: absolute;
      right:30px;
      top: 50%;
      margin-top:-50px;/*높이의 반만큼 되돌아가기*/
    }

    h1{
      font-size: 40px;
    }

    h3{
      margin:20px 0px;
    }

    .title{
      width: 800px;
      height: 200px;
      text-align: center;
      /* background-color: gray; */
      overflow:hidden;
      color:cornsilk;
      position: absolute;
      top: 50%;
      left:50%;
      margin-left:-400px; /*800의 넓이 반만큼 되돌아가기*/
      margin-top:100px;   /*200의 높이 반만큼 되돌아가기*/
    }
    header{
      width:100%;
      line-height: 100px;
      overflow: hidden;
      background-color: rgba(75,130,255,0.54);
      text-align: center;
      color:cornsilk;
      position: fixed;
      left:0;
      top:0;
      z-index:999;
    }
    body{
      height: 3000px;
    }

  </style>
</head>
<body>

  <header>
    topmenu
  </header>

  <div id="mainSlide">
    <button type="button">q</button>
    <button type="button">p</button>

    <div class="title">
      <h1>Lorem Ipsum</h1>
      <h3>What is Lorem Ipsum?</h3>
      <p>Lorem Ipsum is simply dummy text of the printing and
        typesetting industry. Lorem Ipsum has been the industry's s
        tandard dummy text ever since the 1500s.
        when an unknown printer took a galley of type and
        scrambled it to make a type specimen book.
      </p>
    </div>
  </div>

</body>
</html>
```

## 강의 27. position 웹 개발

`nav`를 `fixed`로 고정하고 `section`을 `left` 값으로 밀어 배치하는 좌측 고정 메뉴 레이아웃.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    *{padding:0; margin:0;}
    img{
      display: block;
    }
    body{
      background-color: #808080;
    }
    #wrap{
      width: 1600px;
      overflow:hidden;
      margin:0 auto;
      position: relative;
    }
    nav{
      width: 200px;
      height: 100%;
      position: fixed;
      background-color: black;
    }
    section{
      width: 1400px;
      height: 100%;
      position: relative;
      background-color: yellow;
      /* float: right;  -오른쪽으로 부터 정렬*/
      top:0;
      left:200px;
      overflow: hidden;
    }
    .main{
      width: 1200px;
      overflow: hidden;
      position: relative;
      margin:50px auto; /*1400-1200=200/2=100*/
      height: 399px;
    }
    button{
      width: 100px;
      height: 100px;
      background-color: black;
      border:none;
      border-radius: 50%;
      color:white;
      position: absolute;
      top:50%;
      left: 50%;
      margin-left:-50px;
      margin-top:-50px;
    }
    .banner{
     width: 1160px; /*img(250*4)=1000 + margin(좌우40*4)=160*/
     overflow: hidden;
     margin: 30px auto;
    }
    .banner>img{
      float: left;
      margin:0 20px;
      margin-bottom: 40px;
      box-shadow: 3px 3px 10px yellowgreen;
    }

  </style>
</head>
<body>

  <!-- 전체박스 -->
  <div id="wrap">
    <nav>
      <img src="/HTML5-CSS3/JMJ_27/img/menu.jpg" alt="메뉴">
    </nav>
    <section>
      <div class="main">
        <img src="/HTML5-CSS3/JMJ_27/img/main_pic.jpg" alt="대체이미지">
        <button type="button">play</button>
      </div>
      <div class="banner">

        <img src="/HTML5-CSS3/JMJ_27/img/bn1.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn2.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn3.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn4.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn5.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn6.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn7.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn8.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn9.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn10.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn11.jpg" alt="대체이미지">
        <img src="/HTML5-CSS3/JMJ_27/img/bn12.jpg" alt="대체이미지">
      </div>
    </section>
  </div>
  <!-- //전체박스 -->
</body>
</html>
```

### 메뉴 구현 (좌측 고정 nav)

HTML:

```html
<div id="wrap">
    <nav>
      <h1>1987<br /> DESIGN </h1>
      <ul class="submenu">
        <li><a href="#">MEMBER </a></li>
        <li><a href="#">LOGIN</a></li>
        <li><a href="#">JOIN US </a></li>
        <li><a href="#">CART(0 ITEM)</a></li>
        <li><a href="#">ORDER</a></li>
        <li><a href="#">MY PAGE </a></li>
      </ul>
      <ul class="submenu">
        <li><a href="#">CATEGORY  </a></li>
        <li><a href="#">OUTER   </a></li>
        <li><a href="#">TOP  </a></li>
        <li><a href="#">BOTTOM  </a></li>
        <li><a href="#">ACC  </a></li>
        <li><a href="#">SALE   </a></li>
        <li><a href="#">TODAY VIEW  </a></li>
      </ul>
      <ul class="submenu">
        <li><a href="#">BOARD  </a></li>
        <li><a href="#">NOTICE </a></li>
        <li><a href="#">REVIEW  </a></li>
        <li><a href="#">Q&#62;A </a></li>
      </ul>
      <div class="form">
        <input type="text" name="" />
        <img src="img/sch.jpg" alt="" />
      </div>
    </nav>
</div>
```

CSS:

```css
nav{
    width: 200px;
    height: 100%;
    position: fixed;
    background-color: #000;
}

nav > h1 {
  text-align:center;
  color:#ffd800;
  margin:50px 0px;
  line-height:30px;
}

.submenu {
   width:100px;
   margin:0 auto;
   overflow:hidden;
   margin-bottom:20px;
}
.submenu > li {
  line-height:20px;
 }
.submenu > li a{
    font-size:13px;
    color:#ffffff;
 }
.submenu > li:nth-child(1) {
  font-weight:900;
 }

.form {
  width:120px;
  border:1px solid #333;
  height:30px;
  margin:0 auto;
}
.form input[type=text] {
  width:80px;
  height:30px;
  border:none;
  background-color:#000;
  display:block;
  float:left;
}
.form > img {
  float:right;
  margin:7.5px;
 }
```

## 강의 28. transform

- `transform-origin`: 요소의 중심 기점 변경(x: left/right/center, y: top/bottom/center).
- `translate(x,y)` / `translateX` / `translateY`: 특정 위치로 이동.
- `scale(x,y)` / `scaleX` / `scaleY`: 확대/축소.
- `rotate(deg)` / `rotateX` / `rotateY`: 회전(시계방향, 음수는 반시계).
- `skew(x,y)` / `skewX` / `skewY`: 기울이기(왜곡).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>transform</title>
  <style>
    *{padding: 0; margin: 0;}

    section{
      width: 300px;
      height: 300px;
      border:5px solid black;
      margin:100px;
    }

    div{
      width: 300px;
      height: 300px;
      background-color: rgba(127, 255, 212, 0.132);
      line-height: 300px;
      font-size: 20px;
      font-weight: 900px;
      transform-origin:left bottom
      /*요소의 중심기점을 변경 속성 X,Y (px,%,단어)
        x - left,right,center
        y - top,bottom,center*/
    }
    div:hover{
      transition-duration: 0.5s;

      /* 함께 작성 X,Y */
      transform:translate(100px, 100px);/*특정한 위치로 이동 px,%*/
      transform:translateX(100px); /*x축만큼 이동*/
      transform:translateY(100px); /*y축만큼 이동*/
      transform:scale(1.5,1.5);/*사이즈 확대,축소 - 0.9<1<1.1*/
      transform:scale(0.5,0.5);/*축소*/
      transform:scaleX(2); /*X축으로 값만큼 확대,축소*/
      transform:scaleY(2); /*y축으로 값만큼 확대,축소*/
      transform:rotate(60deg); /*특정한 값만큼 회전 - 각도(deg) 시계방향*/
      transform:rotate(-60deg); /*시계반대방향>>마이너스*/
      transform: rotateX(90deg); /*x축을 기점으로 회전*/
      transform: rotateY(90deg); /*y축을 기점으로 회전*/
      transform: skew(45deg,45deg); /*특정한 각도로 기울이기, 왜곡*/
      transform: skewX(45deg); /*x축으로 기울이기*/
      transform: skewY(45deg); /*y축으로 기울이기*/

      transform: rotate(60deg);
    }

  </style>
</head>
<body>

  <section>
    <div>transform</div>
  </section>

</body>
</html>
```

## 강의 29. transform 응용 (햄버거 메뉴)

`transform` 다중 작성 시 띄어쓰기로 구분한다. 벤더 프리픽스(`-ms-`, `-moz-`, `-webkit-`, `-o-`)로 브라우저별 호환을 준다. 세 줄(`line`)에 `transform`을 조합해 햄버거 버튼이 X자로 변하는 효과를 만든다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>transform</title>
  <style>
    *{padding:0; margin:0;}
    /*div{
      width: 300px;
      height: 300px;
      background-color: aquamarine;
      text-align: center;
      line-height: 300px;
      transform:다중작성 시 띄어쓰기로 구분
      transform:translate(100px,100px) rotate(30deg);
      -ms-transform:translate(100px,100px) rotate(30deg); ie
      -moz-transform:translate(100px,100px) rotate(30deg); 파이어폭스
      -webkit-transform:translate(100px,100px) rotate(30deg); 사파리 크롬
      -o-transform:translate(100px,100px) rotate(30deg); 오페라
    }*/

    header{
      width: 100%;
      height: 100px;
      background-color: aquamarine;
      overflow:hidden
    }
    #ham{
      width: 64px;
      height: 57px;
      padding:22px;
      background-color:#ff9c78;
      overflow: hidden;
      cursor: pointer; /*마우스 커서를 - 손모양*/
    }
    .line{
      background-color: beige;
      width: 56px;
      height: 5px;
      margin:10px 0px;
      transition-duration: 0.5s;
    }

    #main{
      width: 100%;
      overflow: hidden;
      padding:200px 0px;
      background-color: blue;
      text-align: center;
      color: white;
    }
    /* 첫번째 줄 */
    #ham:hover #top{
      transform:translateY(15px) rotate(45deg) ;
      transform-origin: center;
    }
    /* 두번째 줄 */
    #ham:hover #mid{
      opacity: 0;
    }
    #ham:hover #btm{
      transform: translateY(-15px) rotate(-45deg) ;
      transform-origin: center;
    }
  </style>
</head>
<body>

  <header>
    <div id="ham">
      <div class="line" id="top"></div>
      <div class="line" id="mid"></div>
      <div class="line" id="btm"></div>
    </div>
  </header>

  <div id="main">
    <h1>안녕하세요</h1>
    <p>저희 웹페이지에 방문해주셔서 감사합니다.</p>

  </div>

</body>
</html>
```

## 강의 30. transition

동작 구현에 사용하는 속성.

- `transition-duration`: 지속 시간(얼마 동안).
- `transition-delay`: 지연 시간.
- `transition-timing-function`: 시간에 따른 속도. `linear`(일정), `ease`(기본값), `ease-in`(느리게 시작), `ease-out`(느리게 끝), `ease-in-out`(느리게 시작·끝).
- 함께 사용 가능한 속성: 위치, 사이즈, 색상, `transform`.
- `transition`: 속성, 시간, 이징, 지연을 한꺼번에 지정.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* div{
      width: 300px;
      height: 300px;
      background-color: aquamarine;
    }
    div:hover{
      width: 400px;
      height: 400px;
      transition-duration: 0.5s;
    } */
    *{padding:0; margin:0;}
    section{
      width: 700px;
      overflow: hidden;
      padding:30px;
      border:3px solid black;
      margin:150px;
    }
    .line{
      width: 30px;
      height: 30px;
      background-color: blue;
      margin:10px 0px;
      transition-duration: 0.8s;
      /* 동작 구현에 대한 시간 값 - 얼마동안 */
    }
    section:hover{
      width:700px;

    }
    .line:nth-child(1){
      background-color: aliceblue;
      /*transition-delay:0s;  지연시간 후에*/
      transition-timing-function: linear;
      /* 시간에 따른 움직이는 속도의 값 - 일정한 속도*/
    }
    .line:nth-child(2){
      background-color: saddlebrown;
      /*transition-delay:1s;*/
      transition-timing-function: ease;
      /* 기본값 */
    }
    .line:nth-child(3){
      background-color: wheat;
      /*transition-delay:2s;*/
      transition-timing-function: ease-in;
      /* 속도의 시작이 느리게 */
    }
    .line:nth-child(4){
      background-color: firebrick;
      /*transition-delay:3s; */
      transition-timing-function: ease-out;
      /* 속도를 느리게 끝 */
    }
    .line:nth-child(5){
      background-color: rosybrown;
      /*transition-delay:4s;*/
      transition-timing-function: ease-in-out;
      /* 느리게 시작하고 느리게 끝 */
    }

    /* 동작을 부여 할때 함께 사용가능한 속성의 종류
      위치- top,left,right,bottom
      사이즈 - width,height,margin,padding
      색상 - color,background-color,opacity
      변환 속성 - transform

      transition - 한꺼번에 사용 가능
      :속성, 시간 ,이징, 지연
      */
  </style>
</head>
<body>
  <section>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
  </section>
</body>
</html>
```

## 강의 31. transition 응용 (드롭다운 메뉴)

서브메뉴 `ul`의 높이를 `0`으로 숨겼다가 `:hover` 시 높이를 늘리고 `transition-duration`으로 부드럽게 펼치는 메뉴. 가로/세로 두 버전.

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>transition_nav</title>
  <link rel="stylesheet" href="transition_세로.css" type="text/css">
</head>
<body>

  <ul class="menu">
    <li><a href="#">MENU1</a>
        <ul class="submenu">
          <li><a href="#">submenu01</a></li>
          <li><a href="#">submenu02</a></li>
          <li><a href="#">submenu03</a></li>
          <li><a href="#">submenu04</a></li>
          <li><a href="#">submenu05</a></li>
        </ul>
    </li>
    <li><a href="#">MENU2</a>
      <ul class="submenu">
        <li><a href="#">submenu01</a></li>
        <li><a href="#">submenu02</a></li>
        <li><a href="#">submenu03</a></li>
        <li><a href="#">submenu04</a></li>
        <li><a href="#">submenu05</a></li>
      </ul>
  </li>
  <li><a href="#">MENU3</a>
    <ul class="submenu">
      <li><a href="#">submenu01</a></li>
      <li><a href="#">submenu02</a></li>
      <li><a href="#">submenu03</a></li>
      <li><a href="#">submenu04</a></li>
      <li><a href="#">submenu05</a></li>
    </ul>
</li>
<li><a href="#">MENU4</a>
  <ul class="submenu">
    <li><a href="#">submenu01</a></li>
    <li><a href="#">submenu02</a></li>
    <li><a href="#">submenu03</a></li>
    <li><a href="#">submenu04</a></li>
    <li><a href="#">submenu05</a></li>
  </ul>
</li>
<li><a href="#">MENU5</a>
  <ul class="submenu">
    <li><a href="#">submenu01</a></li>
    <li><a href="#">submenu02</a></li>
    <li><a href="#">submenu03</a></li>
    <li><a href="#">submenu04</a></li>
    <li><a href="#">submenu05</a></li>
  </ul>
</li>
  </ul>

</body>
</html>
```

### CSS 가로 버전

```css
*{padding:0; margin:0;}
ul,ol{list-style: none;}
a{text-decoration:none; font-size: 14px;}

/* 가로 메뉴 */
.menu{
 width: 800px;
 overflow: hidden;
 margin:150px auto;
}
.menu>li{
  width: 20%; /*20*5=100%*/
  float: left;
  text-align: center;
  line-height: 40px;
  background-color: aqua;
}
.menu a{
  color: white;
}
.submenu>li{
  line-height: 50px;
  background-color: blue;
}

.submenu{
   height: 0px; /*ul의 높이를 안 보이게 처리*/
   overflow: hidden;
}
.menu>li:hover .submenu{
  height: 250px; /*서브메뉴 li한개의 높이 50*5*/
  transition-duration: 0.5s;
}
.menu>li:hover{
  background-color: blue;
  transition-duration: 1s;
}
```

### CSS 세로 버전

```css
*{padding:0; margin:0;}
ul,ol{list-style: none;}
a{text-decoration:none; font-size: 14px;}

/* 세로 메뉴 */
.menu{
 width: 300px;
 overflow: hidden;
 margin:150px auto;
}
.menu>li{
  width: 100%; /*20*5=100%*/
  text-align: center;
  line-height: 40px;
  background-color: aqua;
}
.menu a{
  color: white;
}
.submenu>li{
  line-height: 50px;
  background-color: blue;
}

.submenu{
   height: 0px; /*ul의 높이를 안 보이게 처리*/
   overflow: hidden;
}
.menu>li:hover .submenu{
  height: 250px; /*서브메뉴 li한개의 높이 50*5*/
  transition-duration: 0.5s;
}
.menu>li:hover{
  background-color: blue;
  transition-duration: 1s;
}
```

## 강의 32. 애니메이션 (@keyframes)

각 프레임 내에서 스타일을 구현해 동작을 만든다.

- `animation-name`: 애니메이션 이름.
- `animation-duration`: 지속 시간.
- `animation-iteration-count`: 횟수(숫자 / `infinite`).
- `animation-direction`: `normal` / `reverse` / `alternate`(from↔to 교차 반복).
- `animation-delay`: 지연.
- `animation-timing-function`: 시간별 속도.
- `animation-play-state`: `paused` / `running`.
- `@keyframes`: 구간별 스타일. `0%`(from, 시작) ~ `100%`(to, 끝), 중간 구간도 표현 가능.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>animation</title>
  <style>
    *{padding:0; margin:0;}
    body{background-color: aquamarine;}

    .ani{
      width: 100px;
      height: 100px;
      position: absolute;
      top:50%;
      left:50%;
      transform:translate(-50px,-50px); /*위치 이동시 margin을 대신하여 사용가능*/
      background-color: beige;
      animation-name:test; /*표현하고자 하는 요소에 애니메이션 이름*/
      animation-duration:2s ;/*애니메이션 동작에 대한 시간-지속될 시간*/
      animation-iteration-count:3;
      /* 애니메이션 횟수=숫자값(횟수),infinite(무한반복)*/
      animation-direction:alternate;
      /* 애니메이션의 방향-normal(기본값)/reverse(반대)/alternate from <->to의 교차반복 */
      animation-delay:1s;/*애니메이션의 지연값*/
      animation-timing-function: ease-in-out;
      /* 시간별 속도감 변화 */
    }

    .ani:hover{
      animation-play-state: paused;
      /* 애니메이션 효과의 재생 혹은 중지 */
    }
    /*키프레임 - 구간별 스타일을 부여하여 동작을 표현
    0%,from>> 시작점
    100%,to>> 끝점

    30%~50%..>> 중간 구간도 표현가능
    */
    @keyframes test{
      0%{
        /* 시작css */
        border-radius: 10px;
        background-color: #ff78a1;
      }
      30%{
        border-radius:30px 0 0 0;
        background-color: #fae573;
      }
      50%{
        border-radius: 0 30px 0 0;
        background-color: #76b47d;
      }
      100%{
        /* 끝css */
        border-radius: 100px;
        background-color: #303efd;
      }
    }
  </style>
</head>
<body>

  <!-- animation: 각각의 프레임 내에서 스타일을 구현하여 동작을 만들때 사용 -->
  <div class="ani"></div>

</body>
</html>
```

## 강의 34. 반응형 웹 - 가변 그리드

- `px`은 고정값, `%`는 부모 폭 기준 비율.
- 공식: `요소의 넓이 / 요소의 부모 넓이 × 100 = 넓이값(%)`.
- `img { max-width: 100%; }`: 부모 기준 최대 100%로 이미지 축소.

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>가변그리드</title>
  <link rel="stylesheet" href="반응형웹.css" type="text/css">
</head>
<body>
  <div id="wrap">
    <header>header</header>
    <section>left</section>
    <aside><img src="/HTML5-CSS3/JMJ_34/사용이미지/bg.jpg"></aside>
    <footer>footer</footer>
  </div>

</body>
</html>
```

### CSS

```css
*{padding:0; margin:0;}


/* px > 고정값
    % > 비율(부모의 폭의 기준으로 양이 결정(=비율))
    공식
    요소의 넓이 /요소의 부모 넓이 = 값*100=넓이값%
    */

img{
  max-width: 100%; /*최대치 - 부모기준으로 최대 100%*/
}
#wrap{
  width: 63.15%;  /*1200/1900=0.6315*100*/
  overflow: hidden;
  margin:150px auto;
  background-color: antiquewhite;
}

header{
  width: 100%;
  height: 100px;
  background-color: aqua;
}
section{
  width: 51.66%; /*620/1200=0.5166*100*/
  float: left;
  height: 200px;
  background-color: blue;
}
aside{
  width: 45%; /*540/1200=0.45*100*/
  float: right;
  height: 200px;
  background-color: brown;

}
footer{
  width: 100%;
  background-color: cornflowerblue;
  height: 100px;
  clear:both; /*float속성을 무시*/
}
```

## 강의 35. 반응형 웹 - 미디어 쿼리

`@media`로 화면 사이즈별 스타일을 분기한다.

- `@media screen and (min-width:1024px)`: 1024px 이상.
- `@media screen and (max-width:1023px)`: 1023px 이하.
- `@media screen and (min-width:480px) and (max-width:767px)`: 480px ~ 767px.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>반응형_미디어쿼리</title>
  <style>
    *{padding:0; margin:0;}
    body{
      background-color: antiquewhite;
    }
    /* @media 미디어쿼리 선언 */
    @media screen and (min-width:1024px){
      /* 내가 보고있는 화면사이즈 1024px이상 화면기준 */
     body{background-color: blue;}
    }
    @media screen and (max-width:1023px){
      /* 내가 보고있는 화면사이즈 1023px이하 화면기준 */
      body{background-color: coral;}
    }
    @media screen and (min-width:480px) and (max-width:767px) {
      /* 480px ~ 767px */
      body{background-color: darksalmon;}

    }
  </style>
</head>
<body>


</body>
</html>
```

## 참고: CSS 속성 정리 (자주 쓰는 태그/속성)

### background

- `background-image: url(" ")`
- `background-repeat: repeat-x`(가로 반복) / `repeat-y`(세로 반복) / `no-repeat`(반복 없음)
- `background-position: right top`(배경 위치 지정)
- `background-attachment: fixed`(스크롤 시 고정) / `scroll`
- 단축 순서: `background-color` → `background-image` → `background-repeat` → `background-attachment` → `background-position`

### border

`border-style`(표시할 테두리 종류):

- `dotted`: 점선 테두리
- `dashed`: 파선 테두리
- `solid`: 실선 테두리
- `double`: 이중 테두리
- `groove`: 3D 그루브 테두리(효과는 border-color에 따라 다름)
- `ridge`: 3D 능선 테두리
- `inset`: 3D 삽입 테두리
- `outset`: 3D 아웃셋 테두리
- `none`: 경계 없음
- `hidden`: 숨겨진 테두리

`border-radius: 5px`: 요소에 둥근 테두리를 추가.

### padding / box-sizing

`box-sizing` 속성을 사용하면 패딩 양에 관계없이 너비를 지정한 값(예: 300px)으로 유지한다.

### height / width

- `auto`: 기본값. 브라우저가 높이·너비를 계산.
- `length`: px, cm 등으로 정의.
- `%`: 컨테이닝 블록의 백분율로 정의.
- `initial`: 기본값으로 설정.
- `inherit`: 부모 값에서 상속.

### outline

요소를 눈에 띄게 하기 위해 테두리 바깥쪽에 그리는 선.

- `outline-style`: `dotted` / `dashed` / `solid` / `double` / `groove` / `ridge` / `inset` / `outset` / `none` / `hidden` (필수 — 이 속성이 설정되지 않으면 다른 outline 속성이 영향을 주지 않는다)
- `outline-color`: 색상 지정(color와 동일)
- `outline-width`: `thin` / `medium` / `thick` / `4px`
- `outline-offset`: 윤곽선과 요소 테두리 사이에 투명한 공간을 추가
- 단축 순서: `outline-width` → `outline-style`(필수) → `outline-color`

### 텍스트

- `color`: 텍스트 색상. `background-color`: 배경 색상.
- 정렬/방향
  - `text-align`: 가로 정렬. `left` / `right` / `center` / `justify`(양쪽 맞춤 — 각 줄을 늘려 좌우 여백을 직선으로).
  - `text-align-last`: 마지막 줄 정렬. `right` / `center` / `justify`.
  - `direction: rtl` + `unicode-bidi: bidi-override`: 텍스트 방향 변경.
  - `vertical-align`: 수직 정렬. `baseline` / `text-top` / `text-bottom` / `sub` / `super`.
- 장식(`text-decoration`)
  - `text-decoration-line`: `overline` / `line-through` / `underline` / `overline underline` (링크가 아닌 텍스트의 밑줄은 혼란을 줄 수 있어 권장하지 않음)
  - `text-decoration-color`: 장식선 색상
  - `text-decoration-style`: `solid` / `double` / `dotted` / `dashed` / `wavy`
  - `text-decoration-thickness`: `auto` / `px` / `%`
  - 단축 순서: `text-decoration-line`(필수) → `text-decoration-color`(선택) → `text-decoration-style`(선택) → `text-decoration-thickness`(선택)
- 변환(`text-transform`): `uppercase` / `lowercase` / `capitalize`
- 간격
  - `text-indent`: 첫 줄 들여쓰기(px)
  - `letter-spacing`: 문자 사이 간격(px)
  - `line-height`: 줄 사이 간격
  - `word-spacing`: 단어 사이 간격(px)
  - `white-space`: 공백 처리 방법(`nowrap` 등)
- 그림자
  - `text-shadow: 수평그림자 수직그림자 흐림효과 색상`

### 글꼴

참고 사이트: w3schools.com
