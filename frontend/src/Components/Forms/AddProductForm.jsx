import './AddSubjectForm.css';
import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { createProduct } from '../../api/products/product.api';
import Button from '../Button/Button';
import toast from 'react-hot-toast';

export default function AddProductForm(props) {

    const [productName, setProductName] = useState('')
    const dispatch = useDispatch();
    const visibleMenu = useSelector((state) => state.addProductMenuState)
    const activeElementId = useSelector((state) => state.activeElementId)

    const handleSubmit = (e, productName) => {
        dispatch({ type: 'CASE_PRODUCT_MENUSTATE', value: !visibleMenu })

        if (!productName) {
            e.preventDefault();
            return
        }
        
        const toastId = toast.loading('Выполняется подготовка карточки');

        createProduct(props.subjectId, productName).then((data) => {
            if (data.status) {
                dispatch({ type: 'CASE_ADD_PRODUCT', value: [data.result] })
                // console.log(data.result);
                toast.success('Карточка готова!', {
                    id: toastId,
                });
            }
        });


        setProductName('');
        e.preventDefault();
    };

    const handleInput = (e) => {

        setProductName(e.target.value);
        e.preventDefault();
    }

    const handleCkick = () => {
        dispatch({ type: 'CASE_SET_ACTIVE_ELEMENT_ID', value: props.subjectId });
        dispatch({ type: 'CASE_PRODUCT_MENUSTATE', value: !visibleMenu });
    }

    if (visibleMenu && activeElementId === props.subjectId) {
        return (
            <div>
                <form className='AddSubjectForm' onSubmit={(e) => handleSubmit(e, productName)}>
                    <div className='InputWrapper'>
                        <input 
                            className={'FormInput'} 
                            name={'input'}
                            value={productName} 
                            onInput={handleInput} 
                            placeholder={'Введите...'}
                        />
                    </div>
                    <button className={'Button'} type="submit">OK</button>
                </form> 
            </div>
        );
    } else {
        return (<Button name={'Добавить продукт'} action={handleCkick}/>)
    }
}
