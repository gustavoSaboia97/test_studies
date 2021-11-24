import pytest
import mock

from src.person_service import PersonService


@pytest.mark.describe('Person Service Tests:')
class TestPersonService:

    def setup(self) -> None:
        self.person_service = PersonService()

    @mock.patch('src.person_service.pandas')
    def test_should_read_person_csv(self, mock_pandas: mock.MagicMock) -> None:
        mock_person_df = mock.MagicMock()

        mock_pandas.read_csv.return_value = mock_person_df

        response = self.person_service._read_person_csv()

        mock_pandas.read_csv.assert_called_once_with('./person.csv')

        assert mock_person_df == response

    @mock.patch('src.person_service.Person')
    @mock.patch('src.person_service.PersonService._read_person_csv')
    def test_should_create_person_list_with_csv_file(self,
                                                     mock_read_person_csv: mock.MagicMock,
                                                     mock_person: mock.MagicMock) -> None:
        rows = [(0, {'NAME': 'Test Name', 'AGE': 10})]

        mock_person_df = mock.MagicMock()

        mock_read_person_csv.return_value = mock_person_df

        mock_person_df.iterrows.return_value = rows

        response = self.person_service.get_person_by_csv_file()

        mock_person.assert_called_once_with(name='Test Name', age=10)

