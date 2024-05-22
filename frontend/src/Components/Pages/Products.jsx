import './Products.css';
import Section from '../Section/Section';
// import getAllProducts from '../../api/products/product.api';
import PageWrapper from './PageWrapper';
import Button from '../Button/Button';
// import { useState, useEffect } from 'react';

import { useSelector, useDispatch } from 'react-redux'

export default function Products(props) {

    const dispatch = useDispatch()

    return (
        <PageWrapper
            pageName={'Продукты'}
            content={
                <div className="Products">
                    {props.data.map((elem) => <Section name={elem.name} key={elem.id} id={elem.id}/>)}
                </div>
            }
        />
    );
}
