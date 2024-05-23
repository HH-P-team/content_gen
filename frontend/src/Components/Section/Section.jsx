import './Section.css';
import { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import ActiveImage from '../ActiveImage/ActiveImage';
import getProducts from '../../api/products/product.api';
import { getImageBySubjectId } from '../../api/images/image.api';
import { getImageByProductId } from '../../api/images/image.api';
import { createProduct } from '../../api/products/product.api';
import Card from '../Card/Card';
import Button from '../Button/Button';

export default function Section(props) {

    const [payload, setPayload] = useState('');

    const dispatch = useDispatch();
    const products = useSelector((state) => state.products)

    useEffect(() => {
        getImageBySubjectId(props.id).then((data) => {
            if (data.status) {
                setPayload(data.result);
            }
        });
    }, []);    

    useEffect(() => {
        getProducts(props.id).then((data) => {
            if (data.status) {
                dispatch({ type: 'CASE_SET_PRODUCTS', value: {subjectId: props.id, product: data.result} });
            }
        });
    }, []);

    const addProduct = (subjectId) => {
        console.log(subjectId);
        createProduct(subjectId).then((data) => {
            console.log(data);
            if (data.status) {
                // console.log(data.result);
                dispatch({ type: 'CASE_ADD_PRODUCT', value: {subjectId: props.id, product: data.result} });
            }
        })
    }
    // console.log(products)
    return (
        <div className="Section">
            <div className='SectionHeader'>
                <div className='SectionHeaderImage'>
                    <ActiveImage data={payload}/>
                </div>
                <div className='SectionTitle'>{props.name}</div>
                <Button name={'Добавить'} action={() => addProduct(props.id)}/>
            </div>
            <div className='SectionContent'>
                {products[props.id] &&
                    products[props.id].map((elem) => <Card 
                        name={elem.name} 
                        key={elem.id} 
                        id={elem.id}
                        request={getImageByProductId}
                        params={elem.id}
                        />)
                    }
            </div>
        </div>
    );
}
