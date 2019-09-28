
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

### 기본 예제 (Base Example)

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

### 스코핑 인스턴스 속성의 중요성 (The Importance of Scoping Instance Properties)

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

### 실제 사례: Axios 로 Vue 리소스 교체하기 (Real-World Example: Replacing Vue Resource with Axios)

[오래된 Vue 리소스(now-retired Vue Resource)](https://medium.com/the-vue-point/retiring-vue-resource-871a82880af4)를 교체한다고 가정해 보자.
당신은 ```this.$http``` 를 통해 request 메서드에 접근함으로써 Axios 라이브러리 대신 그것와 동일한 작업을 수행할 수 있다.

당신이 해야 할 모든 것은 axios 를 당신의 프로젝트에 포함시키는것 뿐이다.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.15.2/axios.js"></script>

<div id="app">
    <ul>
        <li v-for="user in users">{{ user.name }}</li>
    </ul>
</div>
```

```Vue.prototype.$http``` 에 ```axios``` 라는 별명을 부여하라:

```javascript
Vue.prototype.$http = axios
```

그럼 어떠한 Vue 인스턴스에서든지 ```this.$http.get``` 과 같은 메서드를 사용할 수 있다.

```javascript
new Vue({
    el: '#app',
    data: {
        users: []
    },
    created() {
        var vm = this
        this.$http
            .get('https://jsonplaceholder.typicode.com/users')
            .then(function(response) {
                vm.users = response.data
            })
    }
})
```

### 프로토타입 메서드의 문맥 (The Context of Prototype Methods)

당신이 알아차리지 못한 경우, 메서드는 인스턴스 컨텍스트로부터 얻어진 JavaScript 프로토타입에 추가된다.
이는 그것들이 data, 계산된 속성값, 메서드, 또는 인스턴스에 정의된 다른 무엇에라도 접근하기 위하여
```this``` 를 사용할 수 있다는 의미이다.

```$reverseText``` 메서드를 통해 이러한 이점을 활용해 보자:

```javascript
Vue.prototype.$reverseText = function(propertyName) {
    this[propertyName] = this[propertyName]
        .split('')
        .reverse()
        .join('')
}

new Vue({
    data: {
        message: 'Hello',
    },
    created: function() {
        console.log(this.message)  // => "Hello"
        this.$reverseText('message')
        console.log(this.message)  // => "olleH"
    }
})
```

만약 당신이 ES6/2015 arrow function 을 그것의 부모 스코프에 암시적인 bind 로 사용한다면
이 context binding 은 동작하지 않을 것이라는 사실을 명심하라.

```javascript
Vue.prototype.$reverseText = propertyName => {
    this[propertyName] = this[propertyName]
        .split('')
        .reverse()
        .join('')
}
```

이것은 다음의 에러를 throw 할 것이다:

```text
Uncaught TypeError: Cannot read property 'split' of undefined
```

### 이 패턴을 피하고자 할 때 (When To Avoid This Pattern)

프로토타입 속성의 스코핑을 경계하고 있는 한 이러한 패턴을 사용하는 것은 꽤 안전하다. 이 경우 아마 버그를 생성하지 않을 것이다.

그러나 다른 개발자들과 소통할 때 이것은 때때로 혼란을 초래한다.
예를 들어 그들은 아마도 ```this.$http``` 를 보고 "이 Vue 형태가 뭔지 알 수가 없어!" 라고 생각할 것이다.
그리고 그들은 다른 프로젝트로 옮겨갈 것이고 ```this.$http``` 가 정의되지 않는 한 혼란스러워할 것이다.
또는 구글로부터 어떻게 해야 할지 물을지도 모르지만,
이것이 실제로 별칭 아래 Axios 를 사용하고 있다는 것을 깨닫지 못하기 때문에 결과물을 찾을 수는 없을 것이다.

**편리함은 명시성을 희생시킨다.** 컴포넌트를 볼 때, ```$http``` 가 비롯된 부분을 말할 수 없다.
Vue 스스로 그것이 가능할까? 아니면 플러그인? 동료?

그렇다면 대체할 방안은 무엇일까?

### 대체 패턴 (Alternative Patterns)

#### # 모듈 시스템을 사용하지 않을 때 (When Not Using a Module System)

어떠한 모듈 시스템도 없는 어플리케이션에서는 (예를 들어 Webpack 또는 Browserify)
어떠한 JavaScript 강화 프론트엔드와도 종종 함께 사용되는 패턴이 존재한다.
a global ```App``` 객체가 그것이다.
