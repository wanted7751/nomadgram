import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import PhotoActions from "components/PhotoActions";


const FeedPhoto = (props, context) => {
    return (
        <div className={styles.feedPhoto}>
            <header>
                <img
                    src={props.creator.profile_image || require("images/noPhoto.jpg")}
                    alt={props.creator.username}
                />
                <div>
                    <span>{props.creator.username}</span>
                    <span>{props.locations}</span>
                </div>
            </header>
            <img src={props.file} alt={props.caption} />
            <div>
                <PhotoActions number={props.like_count} />
            </div>
        </div>
    );
};


FeedPhoto.PropTypes = {
    creator: PropTypes.shape({
        profile_image: PropTypes.string,
        username: PropTypes.string.isRequired,
    }).isRequired,
    locations: PropTypes.string.isRequired,
    file:PropTypes.string.isRequired,
    like_count: PropTypes.number.isRequired,
    caption: PropTypes.string.isRequired,
    comments: PropTypes.arrayOf(
        PropTypes.shape({
            message: PropTypes.string.isRequired,
            creator: PropTypes.shape({
                profile_image:PropTypes.string,
                username: PropTypes.string.isRequired
            }).isRequired
           
        })
    ).isRequired,
    created_at:PropTypes.string.isRequired
};


export default FeedPhoto;

