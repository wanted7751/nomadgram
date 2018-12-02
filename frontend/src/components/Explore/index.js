import { connect } from "react-redux";
import { actionCreators as userAction } from "redux/modules/user";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
    const { user:{userList} } = state;
    return { 
        userList 
    };
};


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        getExplore: () => {
            dispatch(userAction.getExplore());
        }
    };
};



export default connect(
    mapStateToProps,
  mapDispatchToProps
)(Container);