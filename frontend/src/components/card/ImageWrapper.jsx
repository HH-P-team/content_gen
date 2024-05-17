import { Suspense } from 'react';
import getImageByText from '../../api/image.api';
import './ImageWrapper.css';

import { useEffect, useState } from 'react';


export default function ImageWrapper(props) {

    const [data, setData] = useState([]);

    useEffect(() => {
        getImageByText(props.message).then((data) => {
            if (data.status) {
                setData(data.result);
            }
        });
    }, [data]);

    return (
        <div className="ImageWrapper">
            <Suspense fallback={<div>Loading...</div>}>
                {data ? (<img className="Image" src={"data:image/png;base64, " + data}/>) : (<div></div>)}
            </Suspense>
        </div>
    );
}
