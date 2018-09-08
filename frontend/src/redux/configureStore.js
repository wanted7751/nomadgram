import {createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import {routerReducer, routerMiddleware} from "react-router-redux";
import users from './modules/users';
import createHistory from "history/createBrowserHistory";

const env = process.env.NODE_ENV;

const history = createHistory();

const middlewares = [thunk, routerMiddleware(history)];



if(env === 'development'){
    const {logger} = require("redux-logger");
    middlewares.push(logger);
}

console.log(env);

const reducer = combineReducers({
    users,
    routing: routerReducer

});

let store = initialState =>
  createStore(reducer, applyMiddleware(...middlewares));

export {history};

export default store();