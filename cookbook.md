
![author](https://img.shields.io/badge/author-daesungRa-lightgray.svg?style=flat-square)
![date](https://img.shields.io/badge/date-190925-lightgray.svg?style=flat-square)

# Vue 쿡북!

ref: [Introduction of cookbook](https://vuejs.org/v2/cookbook/)

## Contents

1. [Introduction](#Introduction)
2. [Adding Instance Properties](#Adding-Instance-Properties)

## Introduction

### The Cookbook vs the Guide

쿡북은 가이드와 어떻게 다른가? 왜 필요할까?

- **확실한 집중**: 가이드에서는 본질적으로 이야기를 말한다. 각 섹션은 그 이전 섹션에 대한 지식을 가정하고 그 위에서 진행된다.
쿡북에서는 각 레시피가 독립적으로 존재하는데, 이는 레시피가 일반적인 overview 가 아닌
Vue 의 하나의 특별한 관점에 집중할 수 있다는 의미이다.

- **훌륭한 깊이**: 가이드가 너무 길어지는 것을 피하기 위해 우리는 가장 단순한 예제들을 포함하도록 노력할 것인데,
이는 각 특징에 대한 당신의 이해를 돕기 위함이다. 계속해서 진행한 뒤,
쿡북에서는 흥미로운 방식으로 좀 더 복잡한 형태의 예제들을 포함시킬 수 있다.
또한 각 레시피는 세세한 부분까지 충분히 파악하기 위해 그것이 필요로 하는 만큼 길고 디테일해질 수 있다.

- **JavaScript 학습**: 가이드는 ES5 JavaScript 에 대한 적어도 중급 이상의 숙련도를 가정한다.
예를 들어 어떻게 ```Array.prototype.filter``` 가 list 를 filters 하는 계산된 속성 안에서 동작하는지에 대해 설명하지 않는다.
그러나 쿡북에서는 본질적인 JavaScript 특색(ES6/2015+ 를 포함한)들이
어떻게 더 나은 Vue 어플리케이션을 빌드하도록 우리를 돕는지에 대한 맥락 속에서 설명되어질 것이다.

- **생태계 탐험**: 심화 과정에서는 몇몇의 생태계 지식을 가정한다.
예를 들어 당신이 Webpack 에서 단일 파일 컴포넌트를 사용하기를 원한다면,
우리는 Webpack 의 non-Vue 파트 환경설정을 어떻게 하는지에 대한 설명을 하지 않을 것이다.
쿡북에서는 이러한 생태계적 라이브러리를 더 깊게 살펴볼 수 있는 부분이 마련되어 있다.
- 최소한 Vue 개발자들에게 보편적으로 유용한 범주까지 살펴볼 수 있다.

*주의:* 이러한 모든 차이점에 대해서, 쿡북은 스텝 바이 스텝 매뉴얼이 아님을 명심하라.
이것의 모든 내용에 대해서 당신은 HTML, CSS, JavaScript, npm/yarn 등의 컨셉에 대한 기본적인 이해를 가지고 있다는 것으로 전제된다.

### 쿡북에 기여하기

#### # 우리가 바라는 것

쿡북은 개발자들에게 일반적이거나 흥미로운 use cases 를 다루면서 보다 복잡한 상세 내용을 점진적으로 설명하는 예제를 제공한다.
우리의 목적은 단순하게 개괄적인 예제를 넘어서 보다 광범위하게 적용할 수 있는 개념과 목적지까지의 충분한 유의사항을 설명하는 것에 있다.

-- 이하생략

## Adding Instance Properties

### Base Example

많은 컴포넌트들에 당신이 사용하고자 하는 data/utilities 가 있을 수 있지만,
당신은 [전역 스코프를 오염](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md)시키고 싶지 않을 것이다.
이러한 경우에 당신은 각각의 Vue 인스턴스를 특정 prototype 안에 정의함으로써 그것을 사용 가능하게 할 수 있다.

```javascript
Vue.prototype.$appName = 'My App'
```

이제 ```$appName``` 은 그것을 만들어내기 전에도 모든 인스턴스에서 사용 가능하게 되었다.
만약 다음의 코드를 실행한다면:

```javascript
new Vue({
    beforeCreate: function () {
        console.log(this.$appName)
    }
})
```

```"My App"``` 이란 이름이 콘솔에 기록될 것이다.

### The Importance of Scoping Instance Properties

당신은 아마 다음의 내용이 궁금할지 모른다.

> "왜 ```appName``` 은 ```$``` 로 시작할까? 중요한 것일까? 이것은 어떤 동작을 할까?"

어떤 마법도 일어나지 않는다. ```$``` 는 모든 인스턴스에서 사용 가능한 속성을 지정할 때 Vue 가 사용하는 관례다.
이것은 정의된 어떤 data, 계산된 값이나 메서드와의 충돌도 피할 수 있도록 한다.

> "충돌? 무슨 의미인가?"

좋은 질문이다! 다음을 세팅한다고 가정해 보자:

```javascript
Vue.prototype.appName = 'My App'
```

그럼 하단에 무엇이 기록될 것으로 기대되는가?

```javascript
new Vue({
    data: {
        // Uh oh - appName is *also* the name of the
        // instance property we defined!
        appName: 'The name of some other app'
    },
    beforeCreate: function () {
        console.log(this.appName)
    },
    created: function () {
        console.log(this.appName)
    }
})
```

```"My App"``` 에서 ```"The name of some other app"``` 으로 바뀔 것이다.
왜냐하면 ```this.appName``` 은 인스턴스가 생성될 때 ```data``` 에 의해 덮어씌워지기 때문이다.
우리는 이것을 피하기 위해 인스턴스 속성의 범주를 ```$``` 와 함께 지정할 수 있다.
심지어 플러그인이나 미래의 양식과 충돌하는 것을 미연에 방지하기 위해
당신이 원한다면 ```$_appName``` 이나 ```ΩappName``` 과 같이 당신만의 컨벤션을 사용할 수도 있다.
