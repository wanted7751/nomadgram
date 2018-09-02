import React, { Component } from 'react';
import logo from './logo.svg';
import styles from './App.scss';


class App extends Component {
  render() {
    return (
      <div className={styles.App}>
        <header className={styles.App__header}>
          <img src={logo} className={styles.App__logo} alt="logo" />
          <h1 className={styleMedia.App__title}>Welcome to React</h1>
        </header>
        <p className={styles.App__intro}>
          Park min ho
        </p>
      </div>
    );
  }
}

export default App;
